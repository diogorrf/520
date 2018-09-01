#!/usr/bin/python3

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('digite a sua segunda nota: '))
s = (n1 + n1) / 2
if s >= 7:
    print('Sua primeira nota foi {} e sua segunda nota foi {} e sua media foi {} . Parabéns você foi aprovado'.format(n1, n2, s))
elif s > 3 and s < 7:
    print('Sua primeira nota foi {} e sua segunda nota foi {} e sua media foi {} . Você esta de recuperação'.format(n1, n2, s))
else:
    print('Sua primeira nota foi {} e sua segunda nota foi {} e sua media foi {} . Infelizmente você reprovou'.format(n1, n2, s))
