from linked_list import Nil

def get_list_of_sentences(chapter1='swansway-chapter1.txt'):
    def to_sentences(p):
            for delimiter in '.?!': p = p.replace(delimiter, '|')
            return [s.strip('\" ') for s in p.split('|')]
    with open(chapter1, 'r', encoding='UTF-8') as f:
        paragraphs = f.readlines()

    sentences = [s for p in paragraphs for s in to_sentences(p) if len(s) > 1]
    list_of_sentences = Nil()
    for s in sentences[::-1]:
        list_of_sentences = list_of_sentences.prepend(s)

    return list_of_sentences

def longest_sentence():
    list_of_sentences = get_list_of_sentences()
    new_lst = list_of_sentences.for_each(lambda s: len(s.split()))
    return new_lst.reduce_right(lambda x,y: max(x,y))


if __name__ == '__main__':
    print(longest_sentence())