
"""
def generateYearSet():
    years = [2018]
    date = [3, 2018]
    while date[1] <= 10000:
        date[0] += 26
        date[1] += date[0]//12
        date[0] %= 12
        years.append(date[1])
    print(years)
"""

windows = {2018, 2020, 2022, 2024, 2026, 2029, 2031, 2033, 2035, 2037, 2039, 2042, 2044, 2046, 2048, 2050, 2052, 2055, 2057, 2059, 2061, 2063, 2065, 2068, 2070, 2072, 2074, 2076, 2078, 2081, 2083, 2085, 2087, 2089, 2091, 2094, 2096, 2098, 2100, 2102, 2104, 2107, 2109, 2111, 2113, 2115, 2117, 2120, 2122, 2124, 2126, 2128, 2130, 2133, 2135, 2137, 2139, 2141, 2143, 2146, 2148, 2150, 2152, 2154, 2156, 2159, 2161, 2163, 2165, 2167, 2169, 2172, 2174, 2176, 2178, 2180, 2182, 2185, 2187, 2189, 2191, 2193, 2195, 2198, 2200, 2202, 2204, 2206, 2208, 2211, 2213, 2215, 2217, 2219, 2221, 2224, 2226, 2228, 2230, 2232, 2234, 2237, 2239, 2241, 2243, 2245, 2247, 2250, 2252, 2254, 2256, 2258, 2260, 2263, 2265, 2267, 2269, 2271, 2273, 2276, 2278, 2280, 2282, 2284, 2286, 2289, 2291, 2293, 2295, 2297, 2299, 2302, 2304, 2306, 2308, 2310, 2312, 2315, 2317, 2319, 2321, 2323, 2325, 2328, 2330, 2332, 2334, 2336, 2338, 2341, 2343, 2345, 2347, 2349, 2351, 2354, 2356, 2358, 2360, 2362, 2364, 2367, 2369, 2371, 2373, 2375, 2377, 2380, 2382, 2384, 2386, 2388, 2390, 2393, 2395, 2397, 2399, 2401, 2403, 2406, 2408, 2410, 2412, 2414, 2416, 2419, 2421, 2423, 2425, 2427, 2429, 2432, 2434, 2436, 2438, 2440, 2442, 2445, 2447, 2449, 2451, 2453, 2455, 2458, 2460, 2462, 2464, 2466, 2468, 2471, 2473, 2475, 2477, 2479, 2481, 2484, 2486, 2488, 2490, 2492, 2494, 2497, 2499, 2501, 2503, 2505, 2507, 2510, 2512, 2514, 2516, 2518, 2520, 2523, 2525, 2527, 2529, 2531, 2533, 2536, 2538, 2540, 2542, 2544, 2546, 2549, 2551, 2553, 2555, 2557, 2559, 2562, 2564, 2566, 2568, 2570, 2572, 2575, 2577, 2579, 2581, 2583, 2585, 2588, 2590, 2592, 2594, 2596, 2598, 2601, 2603, 2605, 2607, 2609, 2611, 2614, 2616, 2618, 2620, 2622, 2624, 2627, 2629, 2631, 2633, 2635, 2637, 2640, 2642, 2644, 2646, 2648, 2650, 2653, 2655, 2657, 2659, 2661, 2663, 2666, 2668, 2670, 2672, 2674, 2676, 2679, 2681, 2683, 2685, 2687, 2689, 2692, 2694, 2696, 2698, 2700, 2702, 2705, 2707, 2709, 2711, 2713, 2715, 2718, 2720, 2722, 2724, 2726, 2728, 2731, 2733, 2735, 2737, 2739, 2741, 2744, 2746, 2748, 2750, 2752, 2754, 2757, 2759, 2761, 2763, 2765, 2767, 2770, 2772, 2774, 2776, 2778, 2780, 2783, 2785, 2787, 2789, 2791, 2793, 2796, 2798, 2800, 2802, 2804, 2806, 2809, 2811, 2813, 2815, 2817, 2819, 2822, 2824, 2826, 2828, 2830, 2832, 2835, 2837, 2839, 2841, 2843, 2845, 2848, 2850, 2852, 2854, 2856, 2858, 2861, 2863, 2865, 2867, 2869, 2871, 2874, 2876, 2878, 2880, 2882, 2884, 2887, 2889, 2891, 2893, 2895, 2897, 2900, 2902, 2904, 2906, 2908, 2910, 2913, 2915, 2917, 2919, 2921, 2923, 2926, 2928, 2930, 2932, 2934, 2936, 2939, 2941, 2943, 2945, 2947, 2949, 2952, 2954, 2956, 2958, 2960, 2962, 2965, 2967, 2969, 2971, 2973, 2975, 2978, 2980, 2982, 2984, 2986, 2988, 2991, 2993, 2995, 2997, 2999, 3001, 3004, 3006, 3008, 3010, 3012, 3014, 3017, 3019, 3021, 3023, 3025, 3027, 3030, 3032, 3034, 3036, 3038, 3040, 3043, 3045, 3047, 3049, 3051, 3053, 3056, 3058, 3060, 3062, 3064, 3066, 3069, 3071, 3073, 3075, 3077, 3079, 3082, 3084, 3086, 3088, 3090, 3092, 3095, 3097, 3099, 3101, 3103, 3105, 3108, 3110, 3112, 3114, 3116, 3118, 3121, 3123, 3125, 3127, 3129, 3131, 3134, 3136, 3138, 3140, 3142, 3144, 3147, 3149, 3151, 3153, 3155, 3157, 3160, 3162, 3164, 3166, 3168, 3170, 3173, 3175, 3177, 3179, 3181, 3183, 3186, 3188, 3190, 3192, 3194, 3196, 3199, 3201, 3203, 3205, 3207, 3209, 3212, 3214, 3216, 3218, 3220, 3222, 3225, 3227, 3229, 3231, 3233, 3235, 3238, 3240, 3242, 3244, 3246, 3248, 3251, 3253, 3255, 3257, 3259, 3261, 3264, 3266, 3268, 3270, 3272, 3274, 3277, 3279, 3281, 3283, 3285, 3287, 3290, 3292, 3294, 3296, 3298, 3300, 3303, 3305, 3307, 3309, 3311, 3313, 3316, 3318, 3320, 3322, 3324, 3326, 3329, 3331, 3333, 3335, 3337, 3339, 3342, 3344, 3346, 3348, 3350, 3352, 3355, 3357, 3359, 3361, 3363, 3365, 3368, 3370, 3372, 3374, 3376, 3378, 3381, 3383, 3385, 3387, 3389, 3391, 3394, 3396, 3398, 3400, 3402, 3404, 3407, 3409, 3411, 3413, 3415, 3417, 3420, 3422, 3424, 3426, 3428, 3430, 3433, 3435, 3437, 3439, 3441, 3443, 3446, 3448, 3450, 3452, 3454, 3456, 3459, 3461, 3463, 3465, 3467, 3469, 3472, 3474, 3476, 3478, 3480, 3482, 3485, 3487, 3489, 3491, 3493, 3495, 3498, 3500, 3502, 3504, 3506, 3508, 3511, 3513, 3515, 3517, 3519, 3521, 3524, 3526, 3528, 3530, 3532, 3534, 3537, 3539, 3541, 3543, 3545, 3547, 3550, 3552, 3554, 3556, 3558, 3560, 3563, 3565, 3567, 3569, 3571, 3573, 3576, 3578, 3580, 3582, 3584, 3586, 3589, 3591, 3593, 3595, 3597, 3599, 3602, 3604, 3606, 3608, 3610, 3612, 3615, 3617, 3619, 3621, 3623, 3625, 3628, 3630, 3632, 3634, 3636, 3638, 3641, 3643, 3645, 3647, 3649, 3651, 3654, 3656, 3658, 3660, 3662, 3664, 3667, 3669, 3671, 3673, 3675, 3677, 3680, 3682, 3684, 3686, 3688, 3690, 3693, 3695, 3697, 3699, 3701, 3703, 3706, 3708, 3710, 3712, 3714, 3716, 3719, 3721, 3723, 3725, 3727, 3729, 3732, 3734, 3736, 3738, 3740, 3742, 3745, 3747, 3749, 3751, 3753, 3755, 3758, 3760, 3762, 3764, 3766, 3768, 3771, 3773, 3775, 3777, 3779, 3781, 3784, 3786, 3788, 3790, 3792, 3794, 3797, 3799, 3801, 3803, 3805, 3807, 3810, 3812, 3814, 3816, 3818, 3820, 3823, 3825, 3827, 3829, 3831, 3833, 3836, 3838, 3840, 3842, 3844, 3846, 3849, 3851, 3853, 3855, 3857, 3859, 3862, 3864, 3866, 3868, 3870, 3872, 3875, 3877, 3879, 3881, 3883, 3885, 3888, 3890, 3892, 3894, 3896, 3898, 3901, 3903, 3905, 3907, 3909, 3911, 3914, 3916, 3918, 3920, 3922, 3924, 3927, 3929, 3931, 3933, 3935, 3937, 3940, 3942, 3944, 3946, 3948, 3950, 3953, 3955, 3957, 3959, 3961, 3963, 3966, 3968, 3970, 3972, 3974, 3976, 3979, 3981, 3983, 3985, 3987, 3989, 3992, 3994, 3996, 3998, 4000, 4002, 4005, 4007, 4009, 4011, 4013, 4015, 4018, 4020, 4022, 4024, 4026, 4028, 4031, 4033, 4035, 4037, 4039, 4041, 4044, 4046, 4048, 4050, 4052, 4054, 4057, 4059, 4061, 4063, 4065, 4067, 4070, 4072, 4074, 4076, 4078, 4080, 4083, 4085, 4087, 4089, 4091, 4093, 4096, 4098, 4100, 4102, 4104, 4106, 4109, 4111, 4113, 4115, 4117, 4119, 4122, 4124, 4126, 4128, 4130, 4132, 4135, 4137, 4139, 4141, 4143, 4145, 4148, 4150, 4152, 4154, 4156, 4158, 4161, 4163, 4165, 4167, 4169, 4171, 4174, 4176, 4178, 4180, 4182, 4184, 4187, 4189, 4191, 4193, 4195, 4197, 4200, 4202, 4204, 4206, 4208, 4210, 4213, 4215, 4217, 4219, 4221, 4223, 4226, 4228, 4230, 4232, 4234, 4236, 4239, 4241, 4243, 4245, 4247, 4249, 4252, 4254, 4256, 4258, 4260, 4262, 4265, 4267, 4269, 4271, 4273, 4275, 4278, 4280, 4282, 4284, 4286, 4288, 4291, 4293, 4295, 4297, 4299, 4301, 4304, 4306, 4308, 4310, 4312, 4314, 4317, 4319, 4321, 4323, 4325, 4327, 4330, 4332, 4334, 4336, 4338, 4340, 4343, 4345, 4347, 4349, 4351, 4353, 4356, 4358, 4360, 4362, 4364, 4366, 4369, 4371, 4373, 4375, 4377, 4379, 4382, 4384, 4386, 4388, 4390, 4392, 4395, 4397, 4399, 4401, 4403, 4405, 4408, 4410, 4412, 4414, 4416, 4418, 4421, 4423, 4425, 4427, 4429, 4431, 4434, 4436, 4438, 4440, 4442, 4444, 4447, 4449, 4451, 4453, 4455, 4457, 4460, 4462, 4464, 4466, 4468, 4470, 4473, 4475, 4477, 4479, 4481, 4483, 4486, 4488, 4490, 4492, 4494, 4496, 4499, 4501, 4503, 4505, 4507, 4509, 4512, 4514, 4516, 4518, 4520, 4522, 4525, 4527, 4529, 4531, 4533, 4535, 4538, 4540, 4542, 4544, 4546, 4548, 4551, 4553, 4555, 4557, 4559, 4561, 4564, 4566, 4568, 4570, 4572, 4574, 4577, 4579, 4581, 4583, 4585, 4587, 4590, 4592, 4594, 4596, 4598, 4600, 4603, 4605, 4607, 4609, 4611, 4613, 4616, 4618, 4620, 4622, 4624, 4626, 4629, 4631, 4633, 4635, 4637, 4639, 4642, 4644, 4646, 4648, 4650, 4652, 4655, 4657, 4659, 4661, 4663, 4665, 4668, 4670, 4672, 4674, 4676, 4678, 4681, 4683, 4685, 4687, 4689, 4691, 4694, 4696, 4698, 4700, 4702, 4704, 4707, 4709, 4711, 4713, 4715, 4717, 4720, 4722, 4724, 4726, 4728, 4730, 4733, 4735, 4737, 4739, 4741, 4743, 4746, 4748, 4750, 4752, 4754, 4756, 4759, 4761, 4763, 4765, 4767, 4769, 4772, 4774, 4776, 4778, 4780, 4782, 4785, 4787, 4789, 4791, 4793, 4795, 4798, 4800, 4802, 4804, 4806, 4808, 4811, 4813, 4815, 4817, 4819, 4821, 4824, 4826, 4828, 4830, 4832, 4834, 4837, 4839, 4841, 4843, 4845, 4847, 4850, 4852, 4854, 4856, 4858, 4860, 4863, 4865, 4867, 4869, 4871, 4873, 4876, 4878, 4880, 4882, 4884, 4886, 4889, 4891, 4893, 4895, 4897, 4899, 4902, 4904, 4906, 4908, 4910, 4912, 4915, 4917, 4919, 4921, 4923, 4925, 4928, 4930, 4932, 4934, 4936, 4938, 4941, 4943, 4945, 4947, 4949, 4951, 4954, 4956, 4958, 4960, 4962, 4964, 4967, 4969, 4971, 4973, 4975, 4977, 4980, 4982, 4984, 4986, 4988, 4990, 4993, 4995, 4997, 4999, 5001, 5003, 5006, 5008, 5010, 5012, 5014, 5016, 5019, 5021, 5023, 5025, 5027, 5029, 5032, 5034, 5036, 5038, 5040, 5042, 5045, 5047, 5049, 5051, 5053, 5055, 5058, 5060, 5062, 5064, 5066, 5068, 5071, 5073, 5075, 5077, 5079, 5081, 5084, 5086, 5088, 5090, 5092, 5094, 5097, 5099, 5101, 5103, 5105, 5107, 5110, 5112, 5114, 5116, 5118, 5120, 5123, 5125, 5127, 5129, 5131, 5133, 5136, 5138, 5140, 5142, 5144, 5146, 5149, 5151, 5153, 5155, 5157, 5159, 5162, 5164, 5166, 5168, 5170, 5172, 5175, 5177, 5179, 5181, 5183, 5185, 5188, 5190, 5192, 5194, 5196, 5198, 5201, 5203, 5205, 5207, 5209, 5211, 5214, 5216, 5218, 5220, 5222, 5224, 5227, 5229, 5231, 5233, 5235, 5237, 5240, 5242, 5244, 5246, 5248, 5250, 5253, 5255, 5257, 5259, 5261, 5263, 5266, 5268, 5270, 5272, 5274, 5276, 5279, 5281, 5283, 5285, 5287, 5289, 5292, 5294, 5296, 5298, 5300, 5302, 5305, 5307, 5309, 5311, 5313, 5315, 5318, 5320, 5322, 5324, 5326, 5328, 5331, 5333, 5335, 5337, 5339, 5341, 5344, 5346, 5348, 5350, 5352, 5354, 5357, 5359, 5361, 5363, 5365, 5367, 5370, 5372, 5374, 5376, 5378, 5380, 5383, 5385, 5387, 5389, 5391, 5393, 5396, 5398, 5400, 5402, 5404, 5406, 5409, 5411, 5413, 5415, 5417, 5419, 5422, 5424, 5426, 5428, 5430, 5432, 5435, 5437, 5439, 5441, 5443, 5445, 5448, 5450, 5452, 5454, 5456, 5458, 5461, 5463, 5465, 5467, 5469, 5471, 5474, 5476, 5478, 5480, 5482, 5484, 5487, 5489, 5491, 5493, 5495, 5497, 5500, 5502, 5504, 5506, 5508, 5510, 5513, 5515, 5517, 5519, 5521, 5523, 5526, 5528, 5530, 5532, 5534, 5536, 5539, 5541, 5543, 5545, 5547, 5549, 5552, 5554, 5556, 5558, 5560, 5562, 5565, 5567, 5569, 5571, 5573, 5575, 5578, 5580, 5582, 5584, 5586, 5588, 5591, 5593, 5595, 5597, 5599, 5601, 5604, 5606, 5608, 5610, 5612, 5614, 5617, 5619, 5621, 5623, 5625, 5627, 5630, 5632, 5634, 5636, 5638, 5640, 5643, 5645, 5647, 5649, 5651, 5653, 5656, 5658, 5660, 5662, 5664, 5666, 5669, 5671, 5673, 5675, 5677, 5679, 5682, 5684, 5686, 5688, 5690, 5692, 5695, 5697, 5699, 5701, 5703, 5705, 5708, 5710, 5712, 5714, 5716, 5718, 5721, 5723, 5725, 5727, 5729, 5731, 5734, 5736, 5738, 5740, 5742, 5744, 5747, 5749, 5751, 5753, 5755, 5757, 5760, 5762, 5764, 5766, 5768, 5770, 5773, 5775, 5777, 5779, 5781, 5783, 5786, 5788, 5790, 5792, 5794, 5796, 5799, 5801, 5803, 5805, 5807, 5809, 5812, 5814, 5816, 5818, 5820, 5822, 5825, 5827, 5829, 5831, 5833, 5835, 5838, 5840, 5842, 5844, 5846, 5848, 5851, 5853, 5855, 5857, 5859, 5861, 5864, 5866, 5868, 5870, 5872, 5874, 5877, 5879, 5881, 5883, 5885, 5887, 5890, 5892, 5894, 5896, 5898, 5900, 5903, 5905, 5907, 5909, 5911, 5913, 5916, 5918, 5920, 5922, 5924, 5926, 5929, 5931, 5933, 5935, 5937, 5939, 5942, 5944, 5946, 5948, 5950, 5952, 5955, 5957, 5959, 5961, 5963, 5965, 5968, 5970, 5972, 5974, 5976, 5978, 5981, 5983, 5985, 5987, 5989, 5991, 5994, 5996, 5998, 6000, 6002, 6004, 6007, 6009, 6011, 6013, 6015, 6017, 6020, 6022, 6024, 6026, 6028, 6030, 6033, 6035, 6037, 6039, 6041, 6043, 6046, 6048, 6050, 6052, 6054, 6056, 6059, 6061, 6063, 6065, 6067, 6069, 6072, 6074, 6076, 6078, 6080, 6082, 6085, 6087, 6089, 6091, 6093, 6095, 6098, 6100, 6102, 6104, 6106, 6108, 6111, 6113, 6115, 6117, 6119, 6121, 6124, 6126, 6128, 6130, 6132, 6134, 6137, 6139, 6141, 6143, 6145, 6147, 6150, 6152, 6154, 6156, 6158, 6160, 6163, 6165, 6167, 6169, 6171, 6173, 6176, 6178, 6180, 6182, 6184, 6186, 6189, 6191, 6193, 6195, 6197, 6199, 6202, 6204, 6206, 6208, 6210, 6212, 6215, 6217, 6219, 6221, 6223, 6225, 6228, 6230, 6232, 6234, 6236, 6238, 6241, 6243, 6245, 6247, 6249, 6251, 6254, 6256, 6258, 6260, 6262, 6264, 6267, 6269, 6271, 6273, 6275, 6277, 6280, 6282, 6284, 6286, 6288, 6290, 6293, 6295, 6297, 6299, 6301, 6303, 6306, 6308, 6310, 6312, 6314, 6316, 6319, 6321, 6323, 6325, 6327, 6329, 6332, 6334, 6336, 6338, 6340, 6342, 6345, 6347, 6349, 6351, 6353, 6355, 6358, 6360, 6362, 6364, 6366, 6368, 6371, 6373, 6375, 6377, 6379, 6381, 6384, 6386, 6388, 6390, 6392, 6394, 6397, 6399, 6401, 6403, 6405, 6407, 6410, 6412, 6414, 6416, 6418, 6420, 6423, 6425, 6427, 6429, 6431, 6433, 6436, 6438, 6440, 6442, 6444, 6446, 6449, 6451, 6453, 6455, 6457, 6459, 6462, 6464, 6466, 6468, 6470, 6472, 6475, 6477, 6479, 6481, 6483, 6485, 6488, 6490, 6492, 6494, 6496, 6498, 6501, 6503, 6505, 6507, 6509, 6511, 6514, 6516, 6518, 6520, 6522, 6524, 6527, 6529, 6531, 6533, 6535, 6537, 6540, 6542, 6544, 6546, 6548, 6550, 6553, 6555, 6557, 6559, 6561, 6563, 6566, 6568, 6570, 6572, 6574, 6576, 6579, 6581, 6583, 6585, 6587, 6589, 6592, 6594, 6596, 6598, 6600, 6602, 6605, 6607, 6609, 6611, 6613, 6615, 6618, 6620, 6622, 6624, 6626, 6628, 6631, 6633, 6635, 6637, 6639, 6641, 6644, 6646, 6648, 6650, 6652, 6654, 6657, 6659, 6661, 6663, 6665, 6667, 6670, 6672, 6674, 6676, 6678, 6680, 6683, 6685, 6687, 6689, 6691, 6693, 6696, 6698, 6700, 6702, 6704, 6706, 6709, 6711, 6713, 6715, 6717, 6719, 6722, 6724, 6726, 6728, 6730, 6732, 6735, 6737, 6739, 6741, 6743, 6745, 6748, 6750, 6752, 6754, 6756, 6758, 6761, 6763, 6765, 6767, 6769, 6771, 6774, 6776, 6778, 6780, 6782, 6784, 6787, 6789, 6791, 6793, 6795, 6797, 6800, 6802, 6804, 6806, 6808, 6810, 6813, 6815, 6817, 6819, 6821, 6823, 6826, 6828, 6830, 6832, 6834, 6836, 6839, 6841, 6843, 6845, 6847, 6849, 6852, 6854, 6856, 6858, 6860, 6862, 6865, 6867, 6869, 6871, 6873, 6875, 6878, 6880, 6882, 6884, 6886, 6888, 6891, 6893, 6895, 6897, 6899, 6901, 6904, 6906, 6908, 6910, 6912, 6914, 6917, 6919, 6921, 6923, 6925, 6927, 6930, 6932, 6934, 6936, 6938, 6940, 6943, 6945, 6947, 6949, 6951, 6953, 6956, 6958, 6960, 6962, 6964, 6966, 6969, 6971, 6973, 6975, 6977, 6979, 6982, 6984, 6986, 6988, 6990, 6992, 6995, 6997, 6999, 7001, 7003, 7005, 7008, 7010, 7012, 7014, 7016, 7018, 7021, 7023, 7025, 7027, 7029, 7031, 7034, 7036, 7038, 7040, 7042, 7044, 7047, 7049, 7051, 7053, 7055, 7057, 7060, 7062, 7064, 7066, 7068, 7070, 7073, 7075, 7077, 7079, 7081, 7083, 7086, 7088, 7090, 7092, 7094, 7096, 7099, 7101, 7103, 7105, 7107, 7109, 7112, 7114, 7116, 7118, 7120, 7122, 7125, 7127, 7129, 7131, 7133, 7135, 7138, 7140, 7142, 7144, 7146, 7148, 7151, 7153, 7155, 7157, 7159, 7161, 7164, 7166, 7168, 7170, 7172, 7174, 7177, 7179, 7181, 7183, 7185, 7187, 7190, 7192, 7194, 7196, 7198, 7200, 7203, 7205, 7207, 7209, 7211, 7213, 7216, 7218, 7220, 7222, 7224, 7226, 7229, 7231, 7233, 7235, 7237, 7239, 7242, 7244, 7246, 7248, 7250, 7252, 7255, 7257, 7259, 7261, 7263, 7265, 7268, 7270, 7272, 7274, 7276, 7278, 7281, 7283, 7285, 7287, 7289, 7291, 7294, 7296, 7298, 7300, 7302, 7304, 7307, 7309, 7311, 7313, 7315, 7317, 7320, 7322, 7324, 7326, 7328, 7330, 7333, 7335, 7337, 7339, 7341, 7343, 7346, 7348, 7350, 7352, 7354, 7356, 7359, 7361, 7363, 7365, 7367, 7369, 7372, 7374, 7376, 7378, 7380, 7382, 7385, 7387, 7389, 7391, 7393, 7395, 7398, 7400, 7402, 7404, 7406, 7408, 7411, 7413, 7415, 7417, 7419, 7421, 7424, 7426, 7428, 7430, 7432, 7434, 7437, 7439, 7441, 7443, 7445, 7447, 7450, 7452, 7454, 7456, 7458, 7460, 7463, 7465, 7467, 7469, 7471, 7473, 7476, 7478, 7480, 7482, 7484, 7486, 7489, 7491, 7493, 7495, 7497, 7499, 7502, 7504, 7506, 7508, 7510, 7512, 7515, 7517, 7519, 7521, 7523, 7525, 7528, 7530, 7532, 7534, 7536, 7538, 7541, 7543, 7545, 7547, 7549, 7551, 7554, 7556, 7558, 7560, 7562, 7564, 7567, 7569, 7571, 7573, 7575, 7577, 7580, 7582, 7584, 7586, 7588, 7590, 7593, 7595, 7597, 7599, 7601, 7603, 7606, 7608, 7610, 7612, 7614, 7616, 7619, 7621, 7623, 7625, 7627, 7629, 7632, 7634, 7636, 7638, 7640, 7642, 7645, 7647, 7649, 7651, 7653, 7655, 7658, 7660, 7662, 7664, 7666, 7668, 7671, 7673, 7675, 7677, 7679, 7681, 7684, 7686, 7688, 7690, 7692, 7694, 7697, 7699, 7701, 7703, 7705, 7707, 7710, 7712, 7714, 7716, 7718, 7720, 7723, 7725, 7727, 7729, 7731, 7733, 7736, 7738, 7740, 7742, 7744, 7746, 7749, 7751, 7753, 7755, 7757, 7759, 7762, 7764, 7766, 7768, 7770, 7772, 7775, 7777, 7779, 7781, 7783, 7785, 7788, 7790, 7792, 7794, 7796, 7798, 7801, 7803, 7805, 7807, 7809, 7811, 7814, 7816, 7818, 7820, 7822, 7824, 7827, 7829, 7831, 7833, 7835, 7837, 7840, 7842, 7844, 7846, 7848, 7850, 7853, 7855, 7857, 7859, 7861, 7863, 7866, 7868, 7870, 7872, 7874, 7876, 7879, 7881, 7883, 7885, 7887, 7889, 7892, 7894, 7896, 7898, 7900, 7902, 7905, 7907, 7909, 7911, 7913, 7915, 7918, 7920, 7922, 7924, 7926, 7928, 7931, 7933, 7935, 7937, 7939, 7941, 7944, 7946, 7948, 7950, 7952, 7954, 7957, 7959, 7961, 7963, 7965, 7967, 7970, 7972, 7974, 7976, 7978, 7980, 7983, 7985, 7987, 7989, 7991, 7993, 7996, 7998, 8000, 8002, 8004, 8006, 8009, 8011, 8013, 8015, 8017, 8019, 8022, 8024, 8026, 8028, 8030, 8032, 8035, 8037, 8039, 8041, 8043, 8045, 8048, 8050, 8052, 8054, 8056, 8058, 8061, 8063, 8065, 8067, 8069, 8071, 8074, 8076, 8078, 8080, 8082, 8084, 8087, 8089, 8091, 8093, 8095, 8097, 8100, 8102, 8104, 8106, 8108, 8110, 8113, 8115, 8117, 8119, 8121, 8123, 8126, 8128, 8130, 8132, 8134, 8136, 8139, 8141, 8143, 8145, 8147, 8149, 8152, 8154, 8156, 8158, 8160, 8162, 8165, 8167, 8169, 8171, 8173, 8175, 8178, 8180, 8182, 8184, 8186, 8188, 8191, 8193, 8195, 8197, 8199, 8201, 8204, 8206, 8208, 8210, 8212, 8214, 8217, 8219, 8221, 8223, 8225, 8227, 8230, 8232, 8234, 8236, 8238, 8240, 8243, 8245, 8247, 8249, 8251, 8253, 8256, 8258, 8260, 8262, 8264, 8266, 8269, 8271, 8273, 8275, 8277, 8279, 8282, 8284, 8286, 8288, 8290, 8292, 8295, 8297, 8299, 8301, 8303, 8305, 8308, 8310, 8312, 8314, 8316, 8318, 8321, 8323, 8325, 8327, 8329, 8331, 8334, 8336, 8338, 8340, 8342, 8344, 8347, 8349, 8351, 8353, 8355, 8357, 8360, 8362, 8364, 8366, 8368, 8370, 8373, 8375, 8377, 8379, 8381, 8383, 8386, 8388, 8390, 8392, 8394, 8396, 8399, 8401, 8403, 8405, 8407, 8409, 8412, 8414, 8416, 8418, 8420, 8422, 8425, 8427, 8429, 8431, 8433, 8435, 8438, 8440, 8442, 8444, 8446, 8448, 8451, 8453, 8455, 8457, 8459, 8461, 8464, 8466, 8468, 8470, 8472, 8474, 8477, 8479, 8481, 8483, 8485, 8487, 8490, 8492, 8494, 8496, 8498, 8500, 8503, 8505, 8507, 8509, 8511, 8513, 8516, 8518, 8520, 8522, 8524, 8526, 8529, 8531, 8533, 8535, 8537, 8539, 8542, 8544, 8546, 8548, 8550, 8552, 8555, 8557, 8559, 8561, 8563, 8565, 8568, 8570, 8572, 8574, 8576, 8578, 8581, 8583, 8585, 8587, 8589, 8591, 8594, 8596, 8598, 8600, 8602, 8604, 8607, 8609, 8611, 8613, 8615, 8617, 8620, 8622, 8624, 8626, 8628, 8630, 8633, 8635, 8637, 8639, 8641, 8643, 8646, 8648, 8650, 8652, 8654, 8656, 8659, 8661, 8663, 8665, 8667, 8669, 8672, 8674, 8676, 8678, 8680, 8682, 8685, 8687, 8689, 8691, 8693, 8695, 8698, 8700, 8702, 8704, 8706, 8708, 8711, 8713, 8715, 8717, 8719, 8721, 8724, 8726, 8728, 8730, 8732, 8734, 8737, 8739, 8741, 8743, 8745, 8747, 8750, 8752, 8754, 8756, 8758, 8760, 8763, 8765, 8767, 8769, 8771, 8773, 8776, 8778, 8780, 8782, 8784, 8786, 8789, 8791, 8793, 8795, 8797, 8799, 8802, 8804, 8806, 8808, 8810, 8812, 8815, 8817, 8819, 8821, 8823, 8825, 8828, 8830, 8832, 8834, 8836, 8838, 8841, 8843, 8845, 8847, 8849, 8851, 8854, 8856, 8858, 8860, 8862, 8864, 8867, 8869, 8871, 8873, 8875, 8877, 8880, 8882, 8884, 8886, 8888, 8890, 8893, 8895, 8897, 8899, 8901, 8903, 8906, 8908, 8910, 8912, 8914, 8916, 8919, 8921, 8923, 8925, 8927, 8929, 8932, 8934, 8936, 8938, 8940, 8942, 8945, 8947, 8949, 8951, 8953, 8955, 8958, 8960, 8962, 8964, 8966, 8968, 8971, 8973, 8975, 8977, 8979, 8981, 8984, 8986, 8988, 8990, 8992, 8994, 8997, 8999, 9001, 9003, 9005, 9007, 9010, 9012, 9014, 9016, 9018, 9020, 9023, 9025, 9027, 9029, 9031, 9033, 9036, 9038, 9040, 9042, 9044, 9046, 9049, 9051, 9053, 9055, 9057, 9059, 9062, 9064, 9066, 9068, 9070, 9072, 9075, 9077, 9079, 9081, 9083, 9085, 9088, 9090, 9092, 9094, 9096, 9098, 9101, 9103, 9105, 9107, 9109, 9111, 9114, 9116, 9118, 9120, 9122, 9124, 9127, 9129, 9131, 9133, 9135, 9137, 9140, 9142, 9144, 9146, 9148, 9150, 9153, 9155, 9157, 9159, 9161, 9163, 9166, 9168, 9170, 9172, 9174, 9176, 9179, 9181, 9183, 9185, 9187, 9189, 9192, 9194, 9196, 9198, 9200, 9202, 9205, 9207, 9209, 9211, 9213, 9215, 9218, 9220, 9222, 9224, 9226, 9228, 9231, 9233, 9235, 9237, 9239, 9241, 9244, 9246, 9248, 9250, 9252, 9254, 9257, 9259, 9261, 9263, 9265, 9267, 9270, 9272, 9274, 9276, 9278, 9280, 9283, 9285, 9287, 9289, 9291, 9293, 9296, 9298, 9300, 9302, 9304, 9306, 9309, 9311, 9313, 9315, 9317, 9319, 9322, 9324, 9326, 9328, 9330, 9332, 9335, 9337, 9339, 9341, 9343, 9345, 9348, 9350, 9352, 9354, 9356, 9358, 9361, 9363, 9365, 9367, 9369, 9371, 9374, 9376, 9378, 9380, 9382, 9384, 9387, 9389, 9391, 9393, 9395, 9397, 9400, 9402, 9404, 9406, 9408, 9410, 9413, 9415, 9417, 9419, 9421, 9423, 9426, 9428, 9430, 9432, 9434, 9436, 9439, 9441, 9443, 9445, 9447, 9449, 9452, 9454, 9456, 9458, 9460, 9462, 9465, 9467, 9469, 9471, 9473, 9475, 9478, 9480, 9482, 9484, 9486, 9488, 9491, 9493, 9495, 9497, 9499, 9501, 9504, 9506, 9508, 9510, 9512, 9514, 9517, 9519, 9521, 9523, 9525, 9527, 9530, 9532, 9534, 9536, 9538, 9540, 9543, 9545, 9547, 9549, 9551, 9553, 9556, 9558, 9560, 9562, 9564, 9566, 9569, 9571, 9573, 9575, 9577, 9579, 9582, 9584, 9586, 9588, 9590, 9592, 9595, 9597, 9599, 9601, 9603, 9605, 9608, 9610, 9612, 9614, 9616, 9618, 9621, 9623, 9625, 9627, 9629, 9631, 9634, 9636, 9638, 9640, 9642, 9644, 9647, 9649, 9651, 9653, 9655, 9657, 9660, 9662, 9664, 9666, 9668, 9670, 9673, 9675, 9677, 9679, 9681, 9683, 9686, 9688, 9690, 9692, 9694, 9696, 9699, 9701, 9703, 9705, 9707, 9709, 9712, 9714, 9716, 9718, 9720, 9722, 9725, 9727, 9729, 9731, 9733, 9735, 9738, 9740, 9742, 9744, 9746, 9748, 9751, 9753, 9755, 9757, 9759, 9761, 9764, 9766, 9768, 9770, 9772, 9774, 9777, 9779, 9781, 9783, 9785, 9787, 9790, 9792, 9794, 9796, 9798, 9800, 9803, 9805, 9807, 9809, 9811, 9813, 9816, 9818, 9820, 9822, 9824, 9826, 9829, 9831, 9833, 9835, 9837, 9839, 9842, 9844, 9846, 9848, 9850, 9852, 9855, 9857, 9859, 9861, 9863, 9865, 9868, 9870, 9872, 9874, 9876, 9878, 9881, 9883, 9885, 9887, 9889, 9891, 9894, 9896, 9898, 9900, 9902, 9904, 9907, 9909, 9911, 9913, 9915, 9917, 9920, 9922, 9924, 9926, 9928, 9930, 9933, 9935, 9937, 9939, 9941, 9943, 9946, 9948, 9950, 9952, 9954, 9956, 9959, 9961, 9963, 9965, 9967, 9969, 9972, 9974, 9976, 9978, 9980, 9982, 9985, 9987, 9989, 9991, 9993, 9995, 9998, 10000, 10002}

def main():
    #generateYearSet()
    year = int(input())
    if year in windows:
        print("yes")
    else:
        print("no")
main()