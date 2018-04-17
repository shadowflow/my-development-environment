;ctrl + shift + enter
^+Enter::
; 获取活动窗口的 ID/HWND
; A表示当前激活的窗口

id := WinExist("A")

; 通过id来获取标题
WinGetTitle, title, ahk_id %id%

; 分割出文件名
; 用 - 分割获取的title，第一个为文件名
aa := "-"
rr := StrSplit(title, aa)
filename := rr[1]

; 在filename中查找指定的字符串
py:=".py"
cpp:=".cpp"
IfInString, filename, %py%
{
    Send {End}
    sleep,10
    Send :{Enter}
    return
}
IfInString, filename, %cpp%
{
    Send {End}
    sleep,10
    Send `;{Enter}
    return
}
; Else
; {
;     Sleep, 1
; }

return