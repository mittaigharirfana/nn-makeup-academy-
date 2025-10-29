import requests
import json

# Backend API URL
BASE_URL = "http://localhost:8001/api"

# Small courses data from Excel with detailed theory and practical syllabus
courses = [
    {
        "title": "Basic Eyebrow Shaping & Enhancement",
        "description": "Master the art of eyebrow shaping and filling techniques for a clean, defined look.",
        "category": "Makeup",
        "price": 999,
        "duration": "1 Week",
        "instructor": "Irfana Begum",
        "image": "https://images.unsplash.com/photo-1516975080664-ed2fc6a32937",
        "theory_syllabus": [
            {
                "module": "Module 1: Understanding Eyebrow Shapes",
                "topics": [
                    "Face shape analysis and matching eyebrow shapes",
                    "Different eyebrow shapes: Arched, Straight, Soft-Angled, Rounded",
                    "Golden ratio and eyebrow symmetry",
                    "Analyzing your natural brow shape"
                ]
            },
            {
                "module": "Module 2: Eyebrow Mapping Techniques",
                "topics": [
                    "Understanding the three key points: Start, Arch, End",
                    "Using mapping pencils and measuring tools",
                    "Creating symmetrical brows through mapping",
                    "Common mapping mistakes and how to avoid them"
                ]
            },
            {
                "module": "Module 3: Threading Fundamentals",
                "topics": [
                    "Threading techniques and hand positioning",
                    "Hair removal direction and patterns",
                    "Maintaining natural brow growth",
                    "Safety and hygiene practices"
                ]
            },
            {
                "module": "Module 4: Brow Filling Techniques",
                "topics": [
                    "Choosing the right brow product for your hair type",
                    "Pencil vs. Powder vs. Pomade techniques",
                    "Creating hair-like strokes",
                    "Blending for a natural finish"
                ]
            },
            {
                "module": "Module 5: Brow Products Guide",
                "topics": [
                    "Types of brow products and when to use them",
                    "Color selection based on hair color",
                    "Tools: Spoolie, angled brush, brow razor",
                    "Product layering for long-lasting results"
                ]
            },
            {
                "module": "Module 6: Setting & Finishing",
                "topics": [
                    "Using brow gel and setting sprays",
                    "Soap brow technique for feathered look",
                    "Touch-up techniques throughout the day",
                    "Maintenance tips between threading sessions"
                ]
            }
        ],
        "practical_syllabus": [
            {
                "title": "Eyebrow Shape Analysis",
                "url": "https://www.youtube.com/watch?v=vZVKoXj_lIE",
                "duration": "15 mins"
            },
            {
                "title": "Brow Mapping Step-by-Step",
                "url": "https://www.youtube.com/watch?v=J8YBRVU0azE",
                "duration": "20 mins"
            },
            {
                "title": "Threading Techniques Demo",
                "url": "https://www.youtube.com/watch?v=Zz3MwTXK0p0",
                "duration": "18 mins"
            },
            {
                "title": "Brow Filling with Pencil",
                "url": "https://www.youtube.com/watch?v=tPTl7HimqZg",
                "duration": "12 mins"
            },
            {
                "title": "Choosing & Using Brow Products",
                "url": "https://www.youtube.com/watch?v=XcoJwK0NYBU",
                "duration": "16 mins"
            },
            {
                "title": "Setting Brows for All-Day Wear",
                "url": "https://www.youtube.com/watch?v=9AqCbehrhfA",
                "duration": "10 mins"
            }
        ]
    },
    {
        "title": "Everyday Natural Makeup Look",
        "description": "Learn to create a fresh, radiant, no-makeup look perfect for daily wear.",
        "category": "Makeup",
        "price": 1499,
        "duration": "1 Week",
        "instructor": "Irfana Begum",
        "image": "https://images.unsplash.com/photo-1487412947147-5cebf100ffc2",
        "theory_syllabus": [
            {
                "module": "Module 1: Skin Preparation",
                "topics": [
                    "Understanding your skin type",
                    "Cleansing and toning routine",
                    "Moisturizing for makeup base",
                    "Primer selection and application"
                ]
            },
            {
                "module": "Module 2: Base Routine",
                "topics": [
                    "Choosing the right foundation shade",
                    "Foundation types: BB cream, tinted moisturizer, light coverage",
                    "Application techniques for natural finish",
                    "Buffing and blending methods"
                ]
            },
            {
                "module": "Module 3: Concealing Techniques",
                "topics": [
                    "Color correcting basics",
                    "Under-eye concealing",
                    "Spot concealing for blemishes",
                    "Setting concealer without creasing"
                ]
            },
            {
                "module": "Module 4: Natural Blush Application",
                "topics": [
                    "Choosing blush shades for your skin tone",
                    "Cream vs. powder blush",
                    "Placement for natural flush",
                    "Blending techniques"
                ]
            },
            {
                "module": "Module 5: Eye & Lip Routine",
                "topics": [
                    "Simple eye makeup: mascara and nude shades",
                    "Defining the lash line",
                    "Choosing natural lip colors",
                    "Lip prep and application"
                ]
            }
        ],
        "practical_syllabus": [
            {
                "title": "Skin Prep for Natural Makeup",
                "url": "https://www.youtube.com/watch?v=9oVuwnLKMoY",
                "duration": "14 mins"
            },
            {
                "title": "Applying Natural Base Foundation",
                "url": "https://www.youtube.com/watch?v=HE0MUpQ4A3E",
                "duration": "18 mins"
            },
            {
                "title": "Concealing Like a Pro",
                "url": "https://www.youtube.com/watch?v=qcfzN7DBxQc",
                "duration": "15 mins"
            },
            {
                "title": "Natural Blush Application",
                "url": "https://www.youtube.com/watch?v=6VUGjmrOCxA",
                "duration": "12 mins"
            },
            {
                "title": "Complete Natural Look Tutorial",
                "url": "https://www.youtube.com/watch?v=oq2JnkpAO9U",
                "duration": "20 mins"
            }
        ]
    },
    {
        "title": "Festive Glam Makeup for Beginners",
        "description": "Discover how to create glowing, festive looks for special occasions.",
        "category": "Makeup",
        "price": 1999,
        "duration": "2 Weeks",
        "instructor": "Irfana Begum",
        "image": "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9",
        "theory_syllabus": [
            {
                "module": "Module 1: Highlighting Techniques",
                "topics": [
                    "Understanding face structure for highlighting",
                    "Types of highlighters: Powder, cream, liquid",
                    "Placement points for maximum glow",
                    "Intensity control and blending"
                ]
            },
            {
                "module": "Module 2: Contouring Basics",
                "topics": [
                    "Face shape analysis for contouring",
                    "Choosing contour shades",
                    "Contouring vs. Bronzing",
                    "Step-by-step contouring placement"
                ]
            },
            {
                "module": "Module 3: Glitter Eye Makeup",
                "topics": [
                    "Types of glitter: Pressed, loose, gel",
                    "Eye primer for glitter adhesion",
                    "Creating gradient glitter looks",
                    "Safe application and removal"
                ]
            },
            {
                "module": "Module 4: Lip Blending Techniques",
                "topics": [
                    "Ombre lip techniques",
                    "Lip liner and lipstick combinations",
                    "Choosing bold colors for festive looks",
                    "Long-lasting lip application"
                ]
            },
            {
                "module": "Module 5: Setting Tricks",
                "topics": [
                    "Setting spray vs. setting powder",
                    "Baking technique for long wear",
                    "Touch-up strategies for events",
                    "Making makeup last all night"
                ]
            }
        ],
        "practical_syllabus": [
            {
                "title": "Highlighting for Festive Glow",
                "url": "https://www.youtube.com/watch?v=4f71b8xEqSg",
                "duration": "16 mins"
            },
            {
                "title": "Contouring for Beginners",
                "url": "https://www.youtube.com/watch?v=QKz_1aV2hkg",
                "duration": "18 mins"
            },
            {
                "title": "Glitter Eye Makeup Tutorial",
                "url": "https://www.youtube.com/watch?v=8dJRvUQRNEE",
                "duration": "20 mins"
            },
            {
                "title": "Ombre Lip Technique",
                "url": "https://www.youtube.com/watch?v=VUvlI7_2h0k",
                "duration": "12 mins"
            },
            {
                "title": "Setting Makeup for Long Wear",
                "url": "https://www.youtube.com/watch?v=oDEcf0LZX7Y",
                "duration": "14 mins"
            },
            {
                "title": "Complete Festive Glam Look",
                "url": "https://www.youtube.com/watch?v=wuyWKM73dGY",
                "duration": "25 mins"
            },
            {
                "title": "Party Makeup Tips & Tricks",
                "url": "https://www.youtube.com/watch?v=9Tv79nGcN9I",
                "duration": "18 mins"
            },
            {
                "title": "Festive Eye Makeup Variations",
                "url": "https://www.youtube.com/watch?v=8Y6j6JclPa0",
                "duration": "22 mins"
            }
        ]
    },
    {
        "title": "Nail Care & Polish Basics",
        "description": "A complete guide for nail hygiene, cuticle care, and polish application.",
        "category": "Nail",
        "price": 999,
        "duration": "1 Week",
        "instructor": "Irfana Begum",
        "image": "https://images.unsplash.com/photo-1604654894610-df63bc536371",
        "theory_syllabus": [
            {
                "module": "Module 1: Nail Anatomy",
                "topics": [
                    "Understanding nail structure",
                    "Nail growth cycle and health",
                    "Common nail problems and solutions",
                    "Importance of nail care"
                ]
            },
            {
                "module": "Module 2: Cuticle Care",
                "topics": [
                    "Understanding cuticle function",
                    "Safe cuticle trimming techniques",
                    "Cuticle oils and moisturizers",
                    "When to push vs. trim cuticles"
                ]
            },
            {
                "module": "Module 3: Nail Buffing",
                "topics": [
                    "Types of nail buffers and files",
                    "Buffing technique for shine",
                    "Shaping nails: Square, round, almond, oval",
                    "Filing direction and prevention of splitting"
                ]
            },
            {
                "module": "Module 4: Polish Application",
                "topics": [
                    "Base coat, color, top coat importance",
                    "Brush control and application technique",
                    "Preventing bubbles and streaks",
                    "Cleanup around nails"
                ]
            },
            {
                "module": "Module 5: Aftercare & Maintenance",
                "topics": [
                    "Making polish last longer",
                    "Daily nail care routine",
                    "Safe polish removal",
                    "Nail strengthening tips"
                ]
            }
        ],
        "practical_syllabus": [
            {
                "title": "Understanding Nail Anatomy",
                "url": "https://www.youtube.com/watch?v=L4NMD5u5c9s",
                "duration": "12 mins"
            },
            {
                "title": "Cuticle Care & Trimming",
                "url": "https://www.youtube.com/watch?v=x6g_cKYuV3s",
                "duration": "15 mins"
            },
            {
                "title": "Nail Shaping & Buffing",
                "url": "https://www.youtube.com/watch?v=6r06SWYrGVE",
                "duration": "18 mins"
            },
            {
                "title": "Perfect Polish Application",
                "url": "https://www.youtube.com/watch?v=YcyNJKzU-uo",
                "duration": "16 mins"
            },
            {
                "title": "Nail Care Routine & Maintenance",
                "url": "https://www.youtube.com/watch?v=b-bwjRMFVDI",
                "duration": "14 mins"
            }
        ]
    },
    {
        "title": "Beginner Nail Art Designs",
        "description": "Learn easy, creative nail designs using simple tools.",
        "category": "Nail",
        "price": 1499,
        "duration": "2 Weeks",
        "instructor": "Irfana Begum",
        "image": "https://images.unsplash.com/photo-1519415510236-718bdfcd89c8",
        "theory_syllabus": [
            {
                "module": "Module 1: Dotting Techniques",
                "topics": [
                    "Tools for dotting: Dotting tools, bobby pins, toothpicks",
                    "Creating perfect dots of various sizes",
                    "Dot patterns and designs",
                    "Color combinations for dotting"
                ]
            },
            {
                "module": "Module 2: Floral Nail Art",
                "topics": [
                    "Simple flower designs for beginners",
                    "Brush techniques for petals",
                    "Creating leaves and stems",
                    "Color palettes for floral designs"
                ]
            },
            {
                "module": "Module 3: Using Stickers & Decals",
                "topics": [
                    "Types of nail stickers and decals",
                    "Application technique for stickers",
                    "Sealing stickers with top coat",
                    "Combining stickers with hand-painted designs"
                ]
            },
            {
                "module": "Module 4: Glitter Nail Art",
                "topics": [
                    "Types of glitter: Fine, chunky, holographic",
                    "Glitter gradient technique",
                    "Glitter placement and accent nails",
                    "Removal tips for glitter polish"
                ]
            },
            {
                "module": "Module 5: Matte Finish Techniques",
                "topics": [
                    "Using matte top coat",
                    "Mixing glossy and matte finishes",
                    "Matte nail art designs",
                    "Maintaining matte nails"
                ]
            }
        ],
        "practical_syllabus": [
            {
                "title": "Dotting Tool Nail Art Tutorial",
                "url": "https://www.youtube.com/watch?v=PLtE1ry85Ag",
                "duration": "15 mins"
            },
            {
                "title": "Easy Floral Nail Art",
                "url": "https://www.youtube.com/watch?v=DxiVxgthE6M",
                "duration": "18 mins"
            },
            {
                "title": "Using Nail Stickers & Decals",
                "url": "https://www.youtube.com/watch?v=Z7oWaGk6gV4",
                "duration": "12 mins"
            },
            {
                "title": "Glitter Gradient Nails",
                "url": "https://www.youtube.com/watch?v=KYmHXz_K9bY",
                "duration": "16 mins"
            },
            {
                "title": "Matte Nail Art Designs",
                "url": "https://www.youtube.com/watch?v=fLiCgSgoTjk",
                "duration": "14 mins"
            },
            {
                "title": "5 Easy Nail Art Designs",
                "url": "https://www.youtube.com/watch?v=dO-dPFowtls",
                "duration": "20 mins"
            }
        ]
    },
    {
        "title": "Gel Nail Application & Removal",
        "description": "Get salon-quality results at home with professional gel application and safe removal.",
        "category": "Nail",
        "price": 1999,
        "duration": "2 Weeks",
        "instructor": "Irfana Begum",
        "image": "https://images.unsplash.com/photo-1610992015732-2449b76344bc",
        "theory_syllabus": [
            {
                "module": "Module 1: Understanding Gel Nails",
                "topics": [
                    "Gel polish vs. regular polish",
                    "Benefits and drawbacks of gel nails",
                    "Types of gel: Soft gel vs. hard gel",
                    "UV vs. LED lamps"
                ]
            },
            {
                "module": "Module 2: Nail Preparation",
                "topics": [
                    "Cleaning and sanitizing nails",
                    "Buffing the nail surface",
                    "Dehydrating the nail plate",
                    "Proper nail shaping for gel"
                ]
            },
            {
                "module": "Module 3: Gel Application Process",
                "topics": [
                    "Base coat application technique",
                    "Color coat layering",
                    "Avoiding cuticle flooding",
                    "Capping the free edge"
                ]
            },
            {
                "module": "Module 4: Curing Process",
                "topics": [
                    "Understanding curing times",
                    "Proper lamp positioning",
                    "Checking for proper cure",
                    "Troubleshooting curing issues"
                ]
            },
            {
                "module": "Module 5: Safe Removal",
                "topics": [
                    "Soaking method with acetone",
                    "Foil wrapping technique",
                    "Gentle removal without damage",
                    "Post-removal nail care"
                ]
            }
        ],
        "practical_syllabus": [
            {
                "title": "Introduction to Gel Nails",
                "url": "https://www.youtube.com/watch?v=hOWCyQsxAHw",
                "duration": "14 mins"
            },
            {
                "title": "Gel Nail Prep at Home",
                "url": "https://www.youtube.com/watch?v=s7ypzXrmDQU",
                "duration": "16 mins"
            },
            {
                "title": "Step-by-Step Gel Application",
                "url": "https://www.youtube.com/watch?v=dVqAc7bBwsw",
                "duration": "20 mins"
            },
            {
                "title": "Gel Nail Curing Tips",
                "url": "https://www.youtube.com/watch?v=ym1j5wH2sQs",
                "duration": "12 mins"
            },
            {
                "title": "Safe Gel Nail Removal",
                "url": "https://www.youtube.com/watch?v=O3dGLkLCRDU",
                "duration": "15 mins"
            },
            {
                "title": "Troubleshooting Gel Nails",
                "url": "https://www.youtube.com/watch?v=yFkZRQtqJ_g",
                "duration": "18 mins"
            },
            {
                "title": "Gel Nail Care & Maintenance",
                "url": "https://www.youtube.com/watch?v=JwGkglk9lsY",
                "duration": "14 mins"
            }
        ]
    },
    {
        "title": "Everyday Hairstyling for Beginners",
        "description": "Learn simple hairstyles for daily wear that add charm to your everyday look.",
        "category": "Hair",
        "price": 999,
        "duration": "1 Week",
        "instructor": "Irfana Begum",
        "image": "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e",
        "theory_syllabus": [
            {
                "module": "Module 1: Hair Brushing Basics",
                "topics": [
                    "Choosing the right brush for your hair type",
                    "Detangling techniques",
                    "Brushing wet vs. dry hair",
                    "Preventing hair breakage"
                ]
            },
            {
                "module": "Module 2: Basic Braiding",
                "topics": [
                    "Three-strand braid technique",
                    "French braid basics",
                    "Dutch braid fundamentals",
                    "Side braids and fishtail"
                ]
            },
            {
                "module": "Module 3: Simple Buns",
                "topics": [
                    "Low bun for casual look",
                    "High bun and ponytail",
                    "Messy bun technique",
                    "Securing buns properly"
                ]
            },
            {
                "module": "Module 4: Heat Styling Safety",
                "topics": [
                    "Heat protectant products",
                    "Temperature settings for different hair types",
                    "Using flat iron and curling iron safely",
                    "Minimizing heat damage"
                ]
            },
            {
                "module": "Module 5: Hair Finishing",
                "topics": [
                    "Using hairspray and finishing products",
                    "Controlling flyaways",
                    "Adding shine and texture",
                    "Maintaining styles throughout the day"
                ]
            }
        ],
        "practical_syllabus": [
            {
                "title": "Hair Brushing & Detangling",
                "url": "https://www.youtube.com/watch?v=TIkrVYwauy8",
                "duration": "10 mins"
            },
            {
                "title": "Easy Braids for Beginners",
                "url": "https://www.youtube.com/watch?v=qHodM9KbxqE",
                "duration": "18 mins"
            },
            {
                "title": "Quick & Easy Bun Styles",
                "url": "https://www.youtube.com/watch?v=VW7xXLYVm0I",
                "duration": "15 mins"
            },
            {
                "title": "Heat Styling Basics",
                "url": "https://www.youtube.com/watch?v=xk_Y4uIlBbQ",
                "duration": "16 mins"
            },
            {
                "title": "Finishing Touches for Perfect Hair",
                "url": "https://www.youtube.com/watch?v=jTzYSc7lLmk",
                "duration": "12 mins"
            }
        ]
    },
    {
        "title": "Quick Bridal Hairstyles",
        "description": "Perfect for beginners who want to learn quick, elegant bridal hairstyles.",
        "category": "Hair",
        "price": 1999,
        "duration": "2 Weeks",
        "instructor": "Irfana Begum",
        "image": "https://images.unsplash.com/photo-1605497787716-1b0e5fb4f06e",
        "theory_syllabus": [
            {
                "module": "Module 1: Bridal Hair Preparation",
                "topics": [
                    "Washing and conditioning for volume",
                    "Blow-drying techniques for body",
                    "Teasing and backcombing",
                    "Creating a strong base"
                ]
            },
            {
                "module": "Module 2: Low Bun Styles",
                "topics": [
                    "Classic low bun technique",
                    "Side-swept low bun",
                    "Braided low bun variations",
                    "Securing heavy bridal buns"
                ]
            },
            {
                "module": "Module 3: Elegant Updos",
                "topics": [
                    "French twist updo",
                    "Chignon style",
                    "Twisted updo variations",
                    "Volume and height in updos"
                ]
            },
            {
                "module": "Module 4: Hair Accessories",
                "topics": [
                    "Choosing bridal hair accessories",
                    "Placing flowers and pins",
                    "Using veils and tiaras",
                    "Securing accessories properly"
                ]
            },
            {
                "module": "Module 5: Finishing & Hold",
                "topics": [
                    "Strong hold hairsprays",
                    "Touch-up techniques",
                    "Ensuring all-day wear",
                    "Photography-ready finishing"
                ]
            }
        ],
        "practical_syllabus": [
            {
                "title": "Bridal Hair Prep & Volume",
                "url": "https://www.youtube.com/watch?v=QDnBT23f8wU",
                "duration": "16 mins"
            },
            {
                "title": "Classic Bridal Low Bun",
                "url": "https://www.youtube.com/watch?v=DW7Y3aLNheg",
                "duration": "20 mins"
            },
            {
                "title": "Elegant Updo Tutorial",
                "url": "https://www.youtube.com/watch?v=uJqN0cpkPZM",
                "duration": "22 mins"
            },
            {
                "title": "Braided Bridal Hairstyle",
                "url": "https://www.youtube.com/watch?v=k1DMy5_SJc8",
                "duration": "18 mins"
            },
            {
                "title": "Adding Bridal Accessories",
                "url": "https://www.youtube.com/watch?v=v6zMJCxL_w8",
                "duration": "14 mins"
            },
            {
                "title": "Side-Swept Bridal Style",
                "url": "https://www.youtube.com/watch?v=cC5Q-H9VH_c",
                "duration": "19 mins"
            },
            {
                "title": "Finishing Bridal Hair",
                "url": "https://www.youtube.com/watch?v=0Q8HdTz5YQI",
                "duration": "12 mins"
            },
            {
                "title": "Quick Bridal Hair Variations",
                "url": "https://www.youtube.com/watch?v=9O7s2PXQHXU",
                "duration": "24 mins"
            }
        ]
    },
    {
        "title": "Heatless Curls & Volume Techniques",
        "description": "Learn heat-free curling techniques and easy methods to add bounce and volume.",
        "category": "Hair",
        "price": 1499,
        "duration": "1 Week",
        "instructor": "Irfana Begum",
        "image": "https://images.unsplash.com/photo-1560869713-7d0a29430803",
        "theory_syllabus": [
            {
                "module": "Module 1: Heatless Curling Methods",
                "topics": [
                    "Understanding heatless curling benefits",
                    "Tools: Socks, robe ties, foam rollers, flexi rods",
                    "Hair preparation for best results",
                    "Choosing method based on hair type"
                ]
            },
            {
                "module": "Module 2: Overnight Styling",
                "topics": [
                    "Sock curls technique",
                    "Heatless headband curls",
                    "Pin curls for vintage waves",
                    "Protecting hair while sleeping"
                ]
            },
            {
                "module": "Module 3: Volumizing Techniques",
                "topics": [
                    "Root lifting methods",
                    "Blow-drying for volume",
                    "Using volumizing products",
                    "Backcombing for instant volume"
                ]
            },
            {
                "module": "Module 4: Adding Texture",
                "topics": [
                    "Sea salt spray for beach waves",
                    "Braiding for texture",
                    "Twisting techniques",
                    "Creating natural-looking waves"
                ]
            },
            {
                "module": "Module 5: Maintenance & Care",
                "topics": [
                    "Refreshing curls without restyling",
                    "Using dry shampoo",
                    "Extending curl longevity",
                    "Night routine for curly hair"
                ]
            }
        ],
        "practical_syllabus": [
            {
                "title": "Heatless Curls Methods Overview",
                "url": "https://www.youtube.com/watch?v=d2OtJLBZhNg",
                "duration": "16 mins"
            },
            {
                "title": "Overnight Sock Curls Tutorial",
                "url": "https://www.youtube.com/watch?v=RvIcdIpLHvU",
                "duration": "14 mins"
            },
            {
                "title": "Headband Curls Technique",
                "url": "https://www.youtube.com/watch?v=C5pF1sKG8a0",
                "duration": "12 mins"
            },
            {
                "title": "Volumizing Hair Naturally",
                "url": "https://www.youtube.com/watch?v=JIV3W1jjFWw",
                "duration": "15 mins"
            },
            {
                "title": "Beach Waves Without Heat",
                "url": "https://www.youtube.com/watch?v=p8R4a5VN2Lc",
                "duration": "18 mins"
            },
            {
                "title": "Curl Maintenance & Refresh",
                "url": "https://www.youtube.com/watch?v=c8_LF3f6fXU",
                "duration": "13 mins"
            }
        ]
    }
]

# Add courses to database
print("Starting to add small courses to database...")
print("=" * 60)

for idx, course in enumerate(courses, 1):
    try:
        print(f"\n[{idx}/9] Adding: {course['title']}")
        
        response = requests.post(f"{BASE_URL}/courses", json=course)
        
        if response.status_code == 200:
            result = response.json()
            print(f"✓ Successfully added - Course ID: {result.get('id', 'N/A')}")
        else:
            print(f"✗ Failed to add course")
            print(f"  Status Code: {response.status_code}")
            print(f"  Response: {response.text}")
            
    except Exception as e:
        print(f"✗ Error adding course: {str(e)}")

print("\n" + "=" * 60)
print("Course addition process completed!")
