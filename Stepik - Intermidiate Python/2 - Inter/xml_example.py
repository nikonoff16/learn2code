from xml.etree import ElementTree

tree = ElementTree.parse("example.xml")
root = tree.getroot()
tree.write("example_copy.xml")

# use root = ElementTree.fromstring(string_xml_data) to parse from str

# print(root)
# print(root.tag, root.attrib)
#
# print(root[0][0].text)
# #
# # for child in root:
# #     print(child.tag, child.attrib)
# for element in root.iter("scores"):
#     score_sum = 0
#     for child in element:
#         score_sum += float(child.text)
#     print(score_sum)