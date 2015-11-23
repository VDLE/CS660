
;		int main() line number: 6
;		{ line number: 7
;		   int n; line number: 8
;		   //printf("What factorial(n) do you wish to compute (n=): "); line number: 9
;		   //scanf("%d", &n); line number: 10
;		 line number: 11
;		   iterfact(n); line number: 12
;		   recurfact(n); line number: 13
;		} line number: 14
procentry 
(glob, main)
(cons, 0)
(cons, 1)
;		n line number: 8
(            assign            ,               -               ,               -               ,           (local, 0)          );
args (cons, 1)
valout (local, 0)
call (glob, iterfact)
args (cons, 1)
valout (local, 0)
call (glob, recurfact)
endproc
;		int recurfact(int n) line number: 15
;		{ line number: 16
;		   if (n == 1 || n <= 0) line number: 17
;		   { line number: 18
;		      return 1; line number: 19
;		   } line number: 20
;		   else line number: 21
;		   { line number: 22
;		      return n * recurfact(n - 1); line number: 23
;		   } line number: 24
;		} line number: 25
procentry 
(glob, recurfact)
(cons, 1)
(cons, 0)
;		n == 1 line number: 17
(              eq              ,           (glob, n)           ,           (cons, 1)           ,            i_100000           );
;		n <= 0 line number: 17
(              le              ,           (glob, n)           ,           (cons, 0)           ,            i_100001           );
;		n == 1 || n <= 0 line number: 17
(             ori              ,            i_100000           ,            i_100001           ,            i_100002           );
;		if (n == 1 || n <= 0)
;		   {
;		      return 1;
;		   }
;		   
(             brne             ,            i_100002           ,               0               ,          label_100000         );

(            return            ,               -               ,               -               ,               -               );

;		return 1; line number: 19
(            assign            ,           (cons, 1)           ,               _               ,               ra              );
(              br              ,               _               ,               _               ,     (label, label_100001)     );

(label, label_100000)
(            return            ,               -               ,               -               ,               -               );

args (cons, 1)
;		n - 1 line number: 23
(             sub              ,           (glob, n)           ,           (cons, 1)           ,            i_100003           );
valout i_100003
call (glob, recurfact)
;		n * recurfact(n - 1) line number: 23
(             mult             ,           (glob, n)           ,               ra              ,            i_100004           );
;		return n * recurfact(n - 1); line number: 23
(            assign            ,            i_100004           ,               _               ,               ra              );
(label, label_100001)
endproc
;		int iterfact(int n) line number: 27
;		{ line number: 28
;		   int product = 1; line number: 29
;		   int i = 1; line number: 30
;		   for(i = 2; i <= n; i++) line number: 31
;		   { line number: 32
;		      product = product * i; line number: 33
;		   } line number: 34
;		   return product; line number: 35
;		} line number: 36
procentry 
(glob, iterfact)
(cons, 1)
(cons, 2)
;		product = 1; line number: 29
(            assign            ,           (cons, 1)           ,               -               ,           (local, 0)          );
;		i = 1; line number: 30
(            assign            ,           (cons, 1)           ,               -               ,           (local, 1)          );
;		i = 2 line number: 31
(            assign            ,           (cons, 2)           ,               -               ,           (local, 1)          );
;		for(i = 2; i <= n; i++)   {      product = product * i;   }
(              br              ,               -               ,               -               ,          label_100002         );
(            label             ,               -               ,               -               ,          label_100002         );
;		product * i line number: 33
(             mult             ,           (local, 0)          ,           (local, 1)          ,            i_100005           );
;		product = product * i line number: 33
(            assign            ,            i_100005           ,               -               ,           (local, 0)          );
(            label             ,               -               ,               -               ,          label_100003         );
;		i <= n line number: 31
(              le              ,           (local, 1)          ,           (glob, n)           ,            i_100006           );
(             brne             ,               0               ,            i_100006           ,          label_100002         );
(            return            ,               -               ,               -               ,               -               );

;		return product; line number: 35
(            assign            ,           (local, 0)          ,               _               ,               ra              );
endproc