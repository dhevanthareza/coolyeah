.model small
.code
org 100h

label1 :	jmp label2
	teks1 db "-=UDINUS=-$"
	teks2 db 0ah,0dh,"*POLKE*$"
	teks3 db 0ah,0dh,"DHEVAN MUHAMAD ANTHAREZA$"
	teks4 db 0ah,0dh,"A11.2019.12293$"
label2 :
	mov ah,09h
	mov dx,offset teks1
	int 21h
	mov dx,offset teks2
	int 21h
	mov dx,offset teks3
	int 21h
	mov dx,offset teks4
	int 21h
	int 20h
end label1
