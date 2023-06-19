# init python:
#     def next_rnd_in_list(theList):
#         available_questions = [question for question in theList if question not in used_questions]
#         if len(available_questions) == 0:
#             # All questions have been used, reset the used list
#             used_questions.clear()
#             available_questions = theList
#         renpy.random.shuffle(available_questions)
#         next_question = available_questions[0]
#         used_questions.append(next_question)
#         return next_question

#     question_masterlist4 = ["bpquestion_001", "bpquestion_002", "bpquestion_003", "bpquestion_004", "bpquestion_005", "bpquestion_006", "bpquestion_007", "bpquestion_008", "bpquestion_009", "bpquestion_010"]
#     used_questions = []

#     # question_labels = {
#     #     "bpquestion_001": call_question_bpquestion_001,
#     #     "bpquestion_002": call_question_bpquestion_002,
#     #     "bpquestion_003": call_question_bpquestion_003,
#     #     "bpquestion_004": call_question_bpquestion_004,
#     #     "bpquestion_005": call_question_bpquestion_005,
#     #     "bpquestion_006": call_question_bpquestion_006,
#     #     "bpquestion_007": call_question_bpquestion_007,
#     #     "bpquestion_008": call_question_bpquestion_008,
#     #     "bpquestion_009": call_question_bpquestion_009,
#     #     "bpquestion_010": call_question_bpquestion_010,
#     # }

# label bpquiz1:
#     while True:
#         $ selected_question = next_rnd_in_list(question_masterlist4)
#         jump selected_question

#         if renpy.get_interaction_return() == "pass":
#             # Add code to handle passing the question
#             # You can break the loop or continue to the next question
#             pass
#         else:
#             # Add code to handle failing the question
#             # You can decrement lives or take any other necessary actions
#             pass


# # label call_question_bpquestion_001:
# #     jump bpquestion_001

# # label call_question_bpquestion_002:
# #     jump bpquestion_002

# # label call_question_bpquestion_003:
# #     jump bpquestion_003

# # label call_question_bpquestion_004:
# #     jump bpquestion_004

# # label call_question_bpquestion_005:
# #     jump bpquestion_005

# # label call_question_bpquestion_006:
# #     jump bpquestion_006

# # label call_question_bpquestion_007:
# #     jump bpquestion_007

# # label call_question_bpquestion_008:
# #     jump bpquestion_008

# # label call_question_bpquestion_009:
# #     jump bpquestion_009

# # label call_question_bpquestion_010:
# #     jump bpquestion_010