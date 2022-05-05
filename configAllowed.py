import pandas as pd

print('Bạn muốn thay đổi cấp phép của ứng dụng? (y/n): ', end = ' ')
ans = input()

while(ans != 'y' and ans != 'n'):
    print('Nhập lại tuỳ chọn? (y/n): ', end = ' ')
    ans = input()
    
if ans == 'n':
    print('Thiết lập thành công! không có gì thay đổi')
else:
    loi = True
    while loi:
        try:
            print('Nhập số thứ tự các người muốn cấp phép: ', end = ' ')
            ans = input()
            ans = [int(x) for x in ans.split()]
            
            df = pd.read_excel('CSDL.xlsx')
            
            for i in range(len(df)):
                df['allowed'][i] = False
                
            for i in ans:
                if i in range(len(df)):
                    df['allowed'][i] = True
            df.to_excel('CSDL.xlsx', sheet_name='Trang_tính1', index=False)
            
            loi = False
        except:
            print('Lỗi, thực hiện lại...')
            
print('Thành Công')