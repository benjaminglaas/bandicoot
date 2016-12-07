"""
Test to see if indicators for modified bandicoot are computed correctly.
Indicators are computed from the following functions in "all"
"""

import unittest
from bc_dev.utils import all
from bc_dev.io import read_csv

class TestAll(unittest.TestCase):

    def setUp(self):
        self.user = read_csv("test_indicators","./",
                        warnings=False,describe=False)
        self.r = all(self.user,show_all=True,interaction="physical")
        #Grouping is per default per week.

    def test_active_days(self):
        "User is only present the 6th of January 2014."
        out = {
            "allweek": {
                "allday": {
                    "physical": {
                        "mean": 1.0,
                        "std": 0.0
                    },
                }
            }
        }
        self.assertEqual(out,self.r["active_days"])

    def test_number_of_contacts(self):
        "Contacts are 285 and 371."
        out = {
            "allweek": {
                "allday": {
                    "physical": {
                        "mean": 2.0,
                        "std": 0.0
                    },
                }
            }
        }
        self.assertEqual(out,self.r["number_of_contacts"])

    def test_duration(self):
        "All durations are 1 second."
        out = {
            "allweek": {
                "allday": {
                    "physical": {
                        "mean": {
                            "mean": 1.0,
                            "std": 0.0
                        },
                        "std": {
                            "mean": 0.0,
                            "std": 0.0
                        }
                        
                    },
                }
            }
        }
        self.assertEqual(out,self.r["duration"])

    def test_percent_nocturnal(self):
        "All interactions are within 1 minute and 30 seconds of 8 am."
        out = {
            "allweek": {
                "allday": {
                    "physical": {
                        "mean": 0.0,
                        "std": 0.0
                    },
                }
            }
        }
        self.assertEqual(out,self.r["percent_nocturnal"])

    def test_percent_initiated_conversations(self):
        "There is no 'direction' attribute, therefore 0."
        out = {
            "allweek": {
                "allday": {
                    "physical": {
                        "mean": 0.0,
                        "std": 0.0
                    },
                }
            }
        }
        self.assertEqual(out,self.r["percent_initiated_conversations"])

    def test_percent_initiated_interactions(self):
        "There is no 'direction' attribute, therefore 0."
        out = {
            "allweek": {
                "allday": {
                    "physical": {
                        "mean": 0.0,
                        "std": 0.0
                    },
                }
            }
        }
        self.assertEqual(out,self.r["percent_initiated_interactions"])

    def test_response_delay_text(self):
        "Interaction types are not equal to 'text', so None."
        out = {
            "allweek": {
                "allday": {
                    "physical": {
                        "mean": {
                            "mean": None,
                            "std": None
                        },
                        "std": {
                            "mean": None,
                            "std": None
                        }
                        
                    },
                }
            }
        }
        self.assertEqual(out,self.r["response_delay_text"])

    def test_response_rate_text(self):
        "Interaction types are not equal to 'text', so None."
        out = out = {
            "allweek": {
                "allday": {
                    "physical": {
                        "mean": None,
                        "std": None
                    },
                }
            }
        }
        self.assertEqual(out,self.r["response_rate_text"])

    def test_entropy_of_contacts(self):
        """Shannon entropy is defined as (from entropy function)

        if len(data) == 0:
            return None

        n = sum(data)

        _op = lambda f: f * math.log(f)
        return - sum(_op(float(i) / n) for i in data)

        As there are the correspondent_id's
        285 with 1 interaction
        371 with 9 interactions

        the entropy will be
        -((1/10)*ln(1/10)+(9/10)*ln(9/10)) = 0.3250829733914482,
        """
        
        out = {
            "allweek": {
                "allday": {
                    "physical": {
                        "mean": 0.3250829733914482,
                        "std": 0.0
                    },
                }
            }
        }
        self.assertEqual(out,self.r["entropy_of_contacts"])

    def test_balance_of_contacts(self):
        "Only computed for records having a 'direction'."
        out = {
            "allweek": {
                "allday": {
                    "physical": {
                        "mean": {
                            "mean": None,
                            "std": None
                        },
                        "std": {
                            "mean": None,
                            "std": None
                        }
                        
                    },
                }
            }
        }
        self.assertEqual(out,self.r["balance_of_contacts"])

    def test_interactions_per_contacts(self):
        """
        The mean is 10/2 = 5.
        The variance is defined as
        ((1-5)^2 + (9-5)^2)/2 = 16.0
        The std is therefore
        std = sqrt(16.0) = 4.0
        """
        out = {
            "allweek": {
                "allday": {
                    "physical": {
                        "mean": {
                            "mean": 5.0,
                            "std": 0.0
                        },
                        "std": {
                            "mean": 4.0,
                            "std": 0.0
                        }
                        
                    },
                }
            }
        }
        self.assertEqual(out,self.r["interactions_per_contact"])

    def test_interevent_time(self):
        "All of the events are 10 seconds apart."
        out = {
            "allweek": {
                "allday": {
                    "physical": {
                        "mean": {
                            "mean": 10.0,
                            "std": 0.0
                        },
                        "std": {
                            "mean": 0.0,
                            "std": 0.0
                        }
                        
                    },
                }
            }
        }
        self.assertEqual(out,self.r["interevent_time"])

    def test_percent_pareto_interactions(self):
        """There is 1 contact that contributes to 90 % of the interactions,
        and the other 10 %. 1 contact contributes to more than 80 %, 
        divided by 10 observations give 0.1."""
        
        out = {
            "allweek": {
                "allday": {
                    "physical": {
                        "mean": 0.1,
                        "std": 0.0
                    },
                }
            }
        }
        self.assertEqual(out,self.r["percent_pareto_interactions"])

    def test_percent_pareto_durations(self):
        """Function only looks at 'call' interactions,
        therefore the result is 0.0. Could however be 
        modified to look at all interactions,
        but this will be saved for another time."""
        out = {
            "allweek": {
                "allday": {
                    "physical": {
                        "mean": 0.0,
                        "std": 0.0
                    },
                }
            }
        }
        self.assertEqual(out,self.r["percent_pareto_durations"])

    def test_number_of_interactions(self):
        """10 records."""
        out = {
            "allweek": {
                "allday": {
                    "physical": {
                        "mean": 10.0,
                        "std": 0.0
                    },
                }
            }
        }
        self.assertEqual(out,self.r["number_of_interactions"])

    def test_number_of_interactions_in(self):
        "There is no 'direction' attribute, therefore 0."
        out = {
            "allweek": {
                "allday": {
                    "physical": {
                        "mean": 0.0,
                        "std": 0.0
                    },
                }
            }
        }
        self.assertEqual(out,self.r["number_of_interaction_in"])

    def test_number_of_interactions_out(self):
        "There is no 'direction' attribute, therefore 0."
        out = {
            "allweek": {
                "allday": {
                    "physical": {
                        "mean": 0.0,
                        "std": 0.0
                    },
                }
            }
        }
        self.assertEqual(out,self.r["number_of_interaction_out"])

    def test_number_of_antennas(self):
        """Scalar type datatype. Even though no antennas are provided,
        the output of the 'positions' list is
        [None]. Therefore, taking the len(set(positions)) gives 1."""
        out = {
            "allweek": {
                "allday": {
                        "mean": 1.0,
                        "std": 0.0
                    },
                }
            }

        self.assertEqual(out,self.r["number_of_antennas"])

    def test_entropy_of_antennas(self):
        "No antennase, therefore 0."
        out = {
            "allweek": {
                "allday": {
                        "mean": 0.0,
                        "std": 0.0
                    },
                }
            }
        self.assertEqual(out,self.r["entropy_of_antennas"])

    def test_percent_at_home(self):
        "No antennas, therefore no home."
        out = {
            "allweek": {
                "allday": {
                        "mean": None,
                        "std": None
                    },
                }
            }
        self.assertEqual(out,self.r["percent_at_home"])

    def test_radius_of_gyration(self):
        "No antennas, therefore None."
        out = {
            "allweek": {
                "allday": {
                        "mean": None,
                        "std": None
                    }
                }
            }
        self.assertEqual(out,self.r["radius_of_gyration"])

    def test_frequent_antennas(self):
        """ Since the positions list is [None],
        there is 1 observation. This yields 'mean' = 1.0, since 1 location
        takes up more than 80 % (which is 0.8
        observations)of the total number of positions."""
        out = {
            "allweek": {
                "allday": {
                        "mean": 1.0, 
                        "std": 0.0 
                    },
                }
            }
        self.assertEqual(out,self.r["frequent_antennas"])

    def test_churn_rate(self):
        """ Taking 'statistics' of an empty list. 
        Statistics yields {'mean': , 'std', },
        which here gives 'None' for both."""
        out = {
                "mean": None,
                "std": None
            }

        self.assertEqual(out,self.r["churn_rate"])