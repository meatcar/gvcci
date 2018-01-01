import unittest

import numpy as np

from scoring import contrast_between, clip_between_boundaries, sort_colors_by_closest_counterpart, distance_between_colors

white_hsl = np.array([0, 0, 1])
black_hsl = np.array([0, 0, 0])
red_hsl = np.array([0, 1, 0.5])
red_2_hsl = np.array([0.9999999, 1, 0.5])
dark_red_hsl = np.array([0, 1, 0.2])
light_red_hsl = np.array([0, 1, 0.95])

class ScoringTest(unittest.TestCase):
	def test_contrast_between_black_and_white(self):
		self.assertTrue(20.9 <= contrast_between(white_hsl, black_hsl) <= 21)

	def test_contrast_between_self(self):
		self.assertEqual(contrast_between(white_hsl, white_hsl), 1)
		self.assertEqual(contrast_between(black_hsl, black_hsl), 1)

	def test_contrast_pure_black(self):
		self.assertTrue(5.24 <= contrast_between(black_hsl, red_hsl) <= 5.26)

	def test_clip_between_boundaries_good_value(self):
		clipped = clip_between_boundaries(red_hsl, black_hsl, white_hsl, 1, 1)[0]
		self.assertEqual(clipped[0], red_hsl[0])
		self.assertEqual(clipped[1], red_hsl[1])
		self.assertEqual(clipped[2], red_hsl[2])

	def test_clip_between_boundaries_value_too_dark(self):
		clipped = clip_between_boundaries(dark_red_hsl, black_hsl, white_hsl, 4.5, 1)[0]
		clipped_contrast_black = contrast_between(clipped, black_hsl)
		clipped_contrast_white = contrast_between(clipped, white_hsl)

		self.assertEqual(clipped[0], 0)
		self.assertEqual(clipped[1], 1)
		self.assertTrue(0.4 < clipped[2] < 0.6)
		self.assertTrue(4.5 <= clipped_contrast_black <= 5)
		self.assertTrue(clipped_contrast_white >= 1)

	def test_clip_between_boundaries_value_too_light(self):
		clipped = clip_between_boundaries(light_red_hsl, black_hsl, white_hsl, 4.5, 4.5)[0]
		clipped_contrast_black = contrast_between(clipped, black_hsl)
		clipped_contrast_white = contrast_between(clipped, white_hsl)

		self.assertEqual(clipped[0], 0)
		self.assertEqual(clipped[1], 1)
		self.assertTrue(0.4 < clipped[2])
		self.assertTrue(4.5 <= clipped_contrast_black)
		self.assertTrue(4.5 <= clipped_contrast_white <= 5)

	def test_sorted_by_closest_counterpart_even(self):
		colors = np.array([
			[0, 0, 0],
			[1, 1, 1]
		])

		counterpart = np.array([
			[1, 1, 1],
			[0, 0, 0]
		])

		sorted = sort_colors_by_closest_counterpart(colors, counterpart)

		self.assertEqual(colors.shape, sorted.shape)
		self.assertEqual(sorted[0][0], 1)
		self.assertEqual(sorted[1][0], 0)

	def test_sorted_by_closest_counterpart_duplicates(self):
		colors = np.array([
			[0, 0, 0],
			[1, 1, 1]
		])

		counterpart = np.array([
			[0, 0, 0],
			[0, 0, 0]
		])

		sorted = sort_colors_by_closest_counterpart(colors, counterpart)

		self.assertEqual(colors.shape, sorted.shape)
		self.assertEqual(sorted[0][0], 0)
		self.assertEqual(sorted[1][0], 1)

	def test_sorted_by_closest_counterpart_odd(self):
		colors = np.array([
			[0, 0, 0],
			[1, 1, 1],
			[0.5, 0.5, 0.5]
		])

		counterpart = np.array([
			[1, 1, 1],
			[0.5, 0.5, 0.5],
			[0, 0, 0]
		])

		sorted = sort_colors_by_closest_counterpart(colors, counterpart)

		self.assertEqual(colors.shape, sorted.shape)
		self.assertEqual(sorted[0][0], 1)
		self.assertEqual(sorted[1][0], 0.5)
		self.assertEqual(sorted[2][0], 0)

	def test_distance_between_colors_hue_circle_extremities(self):
		dist = distance_between_colors(red_hsl, red_2_hsl)
		self.assertTrue(dist < 0.01)

	def test_sorted_by_closest_counterpart_bad_case(self):
		bad_blue = np.array([0.5694444, 1.0, 0.5]) # got incorrectly mapped to red, should be cyan
		bad_red = np.array([0.0194444, 1.0, 0.5]) # got incorrectly mapped to cyan, should be red
		ansi_red = np.array([0, 1, 0.5])
		ansi_cyan = np.array([0.5, 1, 0.5])
		sorted = sort_colors_by_closest_counterpart(np.vstack((bad_blue, bad_red)), np.vstack((ansi_red, ansi_cyan)))
		sorted_inv = sort_colors_by_closest_counterpart(np.vstack((bad_red, bad_blue)), np.vstack((ansi_red, ansi_cyan)))

		self.assertEqual(sorted[0][0], sorted_inv[0][0])
		self.assertEqual(sorted[0][0], bad_red[0])

		

if __name__ == '__main__':
    unittest.main()
