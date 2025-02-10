# 시간 초과가 발생하는 경우
def dnapw():
    S, P = map(int, input().split())
    DNA = input()
    DNA_list =[]
    DNA_list.extend(DNA)
    A, C, G, T = map(int, input().split())
    cnt = 0
    test = DNA_list[:P]

    for i in range(1, S-P+2): #여기에서 매번 count로 검사하며 시간이 넘어감감
        if test.count('A') >= A and test.count('C') >= C and test.count('G') >= G and test.count('T') >= T:
            cnt += 1
        
        try:
            test.remove(DNA_list[i-1])
            test.append(DNA_list[i+P-1])
        except IndexError:
            break
    return cnt

print(dnapw())

# 개선 방법

def dnapw():
    S, P = map(int, input().split())
    DNA = input()
    DNA_list =[]
    DNA_list.extend(DNA)
    A, C, G, T = map(int, input().split())
    count_dna = {'A':0, 'C' : 0, 'G' : 0, 'T' : 0} #아예 딕셔너리로 DNA값들을 설정, 0으로 초기화화
    cnt = 0

    for i in range(P): #여기~for j 이전까지 맨 처음 배정받는 문자를 확인인
        count_dna[DNA_list[i]] += 1

    if count_dna['A'] >= A and count_dna['C'] >= C and count_dna['G'] >= G and count_dna['T'] >= T:
            cnt += 1

    for j in range(P, S): # DNA_list의 j번째 요소와 j-p번째 요소를 더하고 빼며 조건에 맞는지 확인하고 맞으면 cnt += 1
        count_dna[DNA_list[j]] += 1
        count_dna[DNA_list[j-P]] -= 1
        if count_dna['A'] >= A and count_dna['C'] >= C and count_dna['G'] >= G and count_dna['T'] >= T:
            cnt += 1

    return cnt

print(dnapw())