import PySimpleGUI as sg
import subprocess
import os
import datetime
import pyperclip
import filecmp

sg.theme('Dark Brown')

BAR_MAX = 100

t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)

def main_menu():
    main_layout = [
           [
           sg.Button('Daily Life', size=(20, 2), enable_events=True, key='daily', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12)),
           sg.Button('Announcemnet', size=(20, 2), enable_events=True, key='announcement', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12)),
           sg.Button('奨学金', size=(20, 2), enable_events=True, key='schoolarship', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12))
       ],
            [
            sg.Button('Calender', size=(20, 2), enable_events=True, key='calender', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12)),
            sg.Button('学校紹介', size=(20, 2), enable_events=True, key='introduction', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12)),
            sg.Button('図書館', size=(20, 2), enable_events=True, key='library', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12))
        ],
            [
            sg.Button('食堂', size=(20, 2), enable_events=True, key='cafeteria', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12)),
            sg.Button('事務連絡', size=(20, 2), enable_events=True, key='communication', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12)),
            sg.Button('部活動', size=(20, 2), enable_events=True, key='club', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12))
        ],
            [
            sg.Button('進路実績', size=(20, 2), enable_events=True, key='path', button_color=('#ffd700', '#008080'), pad=((65, 25),(5,0)), font=('UD デジタル 教科書体 N-R', 12)),
            sg.Button('蜻蛉の軌跡', size=(20, 2), enable_events=True, key='archive', button_color=('#ffd700', '#008080'), pad=((25, 65),(5,0)), font=('UD デジタル 教科書体 N-R', 12))
        ],
            [
            sg.Button('管理者', size=(20, 2), enable_events=True, key='admin', button_color=('#fff', '#daa520'), pad=((180, 180),(20,3)), font=('UD デジタル 教科書体 N-R', 12))
        ]

    ]
    return sg.Window('兵庫県立小野高等学校',main_layout)


def daily_menu():
    daily_layout = [
            [
            sg.Text('画像の挿入', font=('UD デジタル 教科書体 N-R', 15), pad=((105, 105),(10,0)))
        ],
            [
            sg.Text('1. img-systemフォルダーに画像を入れてください。', font=('UD デジタル 教科書体 N-R', 10))
        ],
            [
             sg.Text('2. 画像の挿入ボタンを押してください。', font=('UD デジタル 教科書体 N-R', 10))
        ],
            [
            sg.Button('画像の挿入', size=(15, 1), enable_events=True, key='daily-img', button_color=('#ffd700', '#008080'), pad=((93, 93),(2,0)), font=('UD デジタル 教科書体 N-R', 12))
        ],
            [
            sg.Text('Daily Lifeの編集及び更新', font=('UD デジタル 教科書体 N-R', 15), pad=((31, 31),(20,0)))
        ],
            [
            sg.Button('編集', size=(15, 1), enable_events=True, key='edit', button_color=('#ffd700', '#008080'), pad=((15, 15),(5,0)), font=('UD デジタル 教科書体 N-R', 12)),
            sg.Button('更新', size=(15, 1), enable_events=True, key='daily-update', button_color=('#ffd700', '#008080'), pad=((15, 15),(5,0)), font=('UD デジタル 教科書体 N-R', 12))
        ],
            [
            sg.Button('メニュー画面に戻る', size=(20, 1), enable_events=True, key='back', button_color=('#ffd700', '#008080'), pad=((170, 0),(80,3)), font=('UD デジタル 教科書体 N-R', 10))
        ]

    ]
    return sg.Window('Daily Life', daily_layout)


def announcement_menu():
    announcement_layout = [
            [
            sg.Text('Announcementの編集及び更新', font=('UD デジタル 教科書体 N-R', 15), pad=((29, 29),(10,0)))
        ],
            [
            sg.Button('編集', size=(15, 1), enable_events=True, key='edit', button_color=('#ffd700', '#008080'), pad=((20, 15),(5,0)), font=('UD デジタル 教科書体 N-R', 12)),
            sg.Button('更新', size=(15, 1), enable_events=True, key='announcement-update', button_color=('#ffd700', '#008080'), pad=((15, 20),(5,0)), font=('UD デジタル 教科書体 N-R', 12))
        ],
            [
            sg.Button('メニュー画面に戻る', size=(20, 1), enable_events=True, key='back', button_color=('#ffd700', '#008080'), pad=((170, 0),(80,3)), font=('UD デジタル 教科書体 N-R', 10))
        ]

    ]
    return sg.Window('Announcement', announcement_layout)


def schoolarship_menu():
    schoolarship_layout = [
            [
            sg.Text('奨学金ページの編集及び更新', font=('UD デジタル 教科書体 N-R', 15), pad=((29, 29),(10,0)))
        ],
            [
            sg.Button('編集', size=(15, 1), enable_events=True, key='edit', button_color=('#ffd700', '#008080'), pad=((20, 15),(5,0)), font=('UD デジタル 教科書体 N-R', 12)),
            sg.Button('更新', size=(15, 1), enable_events=True, key='schoolarship-update', button_color=('#ffd700', '#008080'), pad=((15, 20),(5,0)), font=('UD デジタル 教科書体 N-R', 12))
        ],
            [
            sg.Button('メニュー画面に戻る', size=(20, 1), enable_events=True, key='back', button_color=('#ffd700', '#008080'), pad=((170, 0),(80,3)), font=('UD デジタル 教科書体 N-R', 10))
        ]

    ]
    return sg.Window('奨学金', schoolarship_layout)


def calender_menu():
    calender_layout = [
            [
            sg.Text('Calenderの編集及び更新', font=('UD デジタル 教科書体 N-R', 15), pad=((45, 45),(10,0)))
        ],
            [
            sg.Button('編集', size=(15, 1), enable_events=True, key='edit', button_color=('#ffd700', '#008080'), pad=((15, 15),(5,0)), font=('UD デジタル 教科書体 N-R', 12)),
            sg.Button('更新', size=(15, 1), enable_events=True, key='calender-update', button_color=('#ffd700', '#008080'), pad=((15, 15),(5,0)), font=('UD デジタル 教科書体 N-R', 12))
        ],
            [
            sg.Button('メニュー画面に戻る', size=(20, 1), enable_events=True, key='back', button_color=('#ffd700', '#008080'), pad=((170, 0),(80,3)), font=('UD デジタル 教科書体 N-R', 10))
        ]

    ]
    return sg.Window('Calender', calender_layout)


def introduction_menu():
    introduction_layout = [
            [
            sg.Text('画像の挿入', font=('UD デジタル 教科書体 N-R', 15), pad=((175, 175),(10,0)))
        ],
            [
            sg.Text('1. img-systemフォルダーに画像を入れてください。', font=('UD デジタル 教科書体 N-R', 10))
        ],
            [
             sg.Text('2. 画像の挿入ボタンを押してください。', font=('UD デジタル 教科書体 N-R', 10))
        ],
            [
             sg.Text('※ 画像の挿入箇所によって、押すボタンが異なることに注意してください。', font=('UD デジタル 教科書体 N-R', 10))
        ],
            [
            sg.Button('学校紹介', size=(45, 1), enable_events=True, key='introduction-img-school', button_color=('#ffd700', '#008080'), pad=((45, 45),(5,10)), font=('UD デジタル 教科書体 N-R', 12))
        ],
            [
            sg.Button('校長挨拶', size=(20, 1), enable_events=True, key='introduction-img-principal', button_color=('#ffd700', '#008080'), pad=((46, 15),(5,0)), font=('UD デジタル 教科書体 N-R', 12)),
            sg.Button('カード要素の画像', size=(20, 1), enable_events=True, key='introduction-img-card', button_color=('#ffd700', '#008080'), pad=((15, 46),(5,0)), font=('UD デジタル 教科書体 N-R', 12))
        ],
            [
            sg.Text('学校紹介ページの編集及び更新', font=('UD デジタル 教科書体 N-R', 15), pad=((85, 85),(20,0)))
        ],
            [
            sg.Button('編集', size=(20, 1), enable_events=True, key='edit', button_color=('#ffd700', '#008080'), pad=((45, 15),(5,0)), font=('UD デジタル 教科書体 N-R', 12)),
            sg.Button('更新', size=(20, 1), enable_events=True, key='introduction-update', button_color=('#ffd700', '#008080'), pad=((15, 45),(5,0)), font=('UD デジタル 教科書体 N-R', 12))
        ],
            [
            sg.Button('メニュー画面に戻る', size=(20, 1), enable_events=True, key='back', button_color=('#ffd700', '#008080'), pad=((310, 0),(80,3)), font=('UD デジタル 教科書体 N-R', 10))
        ]

    ]
    return sg.Window('学校紹介',introduction_layout)


def library_menu():
    library_layout = [
            [
            sg.Text('図書館ページの編集及び更新', font=('UD デジタル 教科書体 N-R', 15), pad=((24, 24),(10,0)))
        ],
            [
            sg.Button('編集', size=(15, 1), enable_events=True, key='edit', button_color=('#ffd700', '#008080'), pad=((15, 15),(5,0)), font=('UD デジタル 教科書体 N-R', 12)),
            sg.Button('更新', size=(15, 1), enable_events=True, key='library-update', button_color=('#ffd700', '#008080'), pad=((15, 15),(5,0)), font=('UD デジタル 教科書体 N-R', 12))
        ],
            [
            sg.Button('メニュー画面に戻る', size=(20, 1), enable_events=True, key='back', button_color=('#ffd700', '#008080'), pad=((170, 0),(80,3)), font=('UD デジタル 教科書体 N-R', 10))
        ]

    ]
    return sg.Window('図書館', library_layout)


def cafeteria_menu():
    cafeteria_layout = [
            [
            sg.Text('食堂営業ページの編集及び更新', font=('UD デジタル 教科書体 N-R', 15), pad=((12, 12),(10,0)))
        ],
            [
            sg.Button('編集', size=(15, 1), enable_events=True, key='edit', button_color=('#ffd700', '#008080'), pad=((15, 15),(5,0)), font=('UD デジタル 教科書体 N-R', 12)),
            sg.Button('更新', size=(15, 1), enable_events=True, key='cafeteria-update', button_color=('#ffd700', '#008080'), pad=((15, 15),(5,0)), font=('UD デジタル 教科書体 N-R', 12))
        ],
            [
            sg.Button('メニュー画面に戻る', size=(20, 1), enable_events=True, key='back', button_color=('#ffd700', '#008080'), pad=((170, 0),(80,3)), font=('UD デジタル 教科書体 N-R', 10))
        ]

    ]
    return sg.Window('食堂', cafeteria_layout)


def communication_menu():
    communication_layout = [
            [
            sg.Text('事務連絡ページの編集及び更新', font=('UD デジタル 教科書体 N-R', 15), pad=((12, 12),(10,0)))
        ],
            [
            sg.Button('編集', size=(15, 1), enable_events=True, key='edit', button_color=('#ffd700', '#008080'), pad=((15, 15),(5,0)), font=('UD デジタル 教科書体 N-R', 12)),
            sg.Button('更新', size=(15, 1), enable_events=True, key='communication-update', button_color=('#ffd700', '#008080'), pad=((15, 15),(5,0)), font=('UD デジタル 教科書体 N-R', 12))
        ],
            [
            sg.Button('メニュー画面に戻る', size=(20, 1), enable_events=True, key='back', button_color=('#ffd700', '#008080'), pad=((170, 0),(80,3)), font=('UD デジタル 教科書体 N-R', 10))
        ]

    ]
    return sg.Window('事務連絡', communication_layout)












def club_menu():
    club_menu_layout = [
            [
            sg.Text('各部活動ページの編集及び更新', font=('UD デジタル 教科書体 N-R', 15), pad=((19, 19),(10,0)))
        ],
            [
            sg.Button('各部活動', size=(15, 1), enable_events=True, key='each-club', button_color=('#ffd700', '#008080'), pad=((85, 85),(2,0)), font=('UD デジタル 教科書体 N-R', 14))
        ],
            [
            sg.Text('部活動のハブページの編集及び更新', font=('UD デジタル 教科書体 N-R', 15), pad=((0, 0),(50,0)))
        ],
            [
            sg.Button('部活動のハブページ', size=(20, 1), enable_events=True, key='club-hub-page', button_color=('#ffd700', '#008080'), pad=((80, 80),(5,0)), font=('UD デジタル 教科書体 N-R', 12))
        ],
            [
            sg.Button('メニュー画面に戻る', size=(20, 1), enable_events=True, key='back', button_color=('#ffd700', '#008080'), pad=((170, 0),(80,3)), font=('UD デジタル 教科書体 N-R', 10))
        ]

    ]
    return sg.Window('部活動', club_menu_layout)

def club_hub_page():
    club_hub_page_layout = [
            [
            sg.Text('画像の挿入', font=('UD デジタル 教科書体 N-R', 15), pad=((105, 105),(10,0)))
        ],
            [
            sg.Text('1. img-systemフォルダーに画像を入れてください。', font=('UD デジタル 教科書体 N-R', 10))
        ],
            [
             sg.Text('2. 画像の挿入ボタンを押してください。', font=('UD デジタル 教科書体 N-R', 10))
        ],
            [
            sg.Button('画像の挿入', size=(15, 1), enable_events=True, key='club-hub-page-img', button_color=('#ffd700', '#008080'), pad=((93, 93),(2,0)), font=('UD デジタル 教科書体 N-R', 12))
        ],
            [
            sg.Text('部活動のハブページの編集及び更新', font=('UD デジタル 教科書体 N-R', 15), pad=((0, 0),(20,0)))
        ],
            [
            sg.Button('編集', size=(15, 1), enable_events=True, key='edit', button_color=('#ffd700', '#008080'), pad=((15, 15),(5,0)), font=('UD デジタル 教科書体 N-R', 12)),
            sg.Button('更新', size=(15, 1), enable_events=True, key='club-hub-page-update', button_color=('#ffd700', '#008080'), pad=((15, 15),(5,0)), font=('UD デジタル 教科書体 N-R', 12))
        ],
            [
            sg.Button('メニュー画面に戻る', size=(20, 1), enable_events=True, key='back', button_color=('#ffd700', '#008080'), pad=((170, 0),(80,3)), font=('UD デジタル 教科書体 N-R', 10))
        ]

    ]
    return sg.Window('部活動のハブページ', club_hub_page_layout)

def each_club():
    each_club_layout = [
            [
            sg.Text('運動部', font=('UD デジタル 教科書体 N-R', 15), pad=((295, 295),(10,0)))
        ],
           [
           sg.Button('野球部', size=(25, 2), enable_events=True, key='baseball', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12)),
           sg.Button('陸上競技部', size=(25, 2), enable_events=True, key='track-and-field', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12)),
           sg.Button('ソフトボール部', size=(25, 2), enable_events=True, key='softball', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12))
       ],
            [
            sg.Button('サッカー部', size=(25, 2), enable_events=True, key='soccer', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12)),
            sg.Button('水泳部', size=(25, 2), enable_events=True, key='swimming', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12)),
            sg.Button('男子テニス部', size=(25, 2), enable_events=True, key='tennis-men', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12))
        ],
            [
            sg.Button('男子ソフトテニス部', size=(25, 2), enable_events=True, key='soft-tennis-men', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12)),
            sg.Button('女子ソフトテニス部', size=(25, 2), enable_events=True, key='soft-tennis-women', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12)),
            sg.Button('男子バスケットボール部', size=(25, 2), enable_events=True, key='basketball-men', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12))
        ],
            [
            sg.Button('女子バスケットボール部', size=(25, 2), enable_events=True, key='basketball-women', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12)),
            sg.Button('男子バレーボール部', size=(25, 2), enable_events=True, key='volleyball-men', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12)),
            sg.Button('女子バレーボール部', size=(25, 2), enable_events=True, key='volleyball-women', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12))
        ],
            [
            sg.Button('男子卓球部', size=(25, 2), enable_events=True, key='ping-pong-men', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12)),
            sg.Button('女子卓球部', size=(25, 2), enable_events=True, key='ping-pong-women', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12)),
            sg.Button('柔道部', size=(25, 2), enable_events=True, key='judo', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12))
        ],
                    [
            sg.Button('剣道部', size=(25, 2), enable_events=True, key='kendo', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12)),
            sg.Button('空手部', size=(25, 2), enable_events=True, key='karate', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12)),
            sg.Button('ダンス部', size=(25, 2), enable_events=True, key='dance', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12))
        ],
            [
            sg.Text('文化部', font=('UD デジタル 教科書体 N-R', 15), pad=((295, 295),(10,0)))
        ],
           [
           sg.Button('吹奏楽部', size=(25, 2), enable_events=True, key='brassband', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12)),
           sg.Button('放送部', size=(25, 2), enable_events=True, key='school-broardcasting', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12)),
           sg.Button('ギター部', size=(25, 2), enable_events=True, key='guitar', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12))
       ],
            [
           sg.Button('書道部', size=(25, 2), enable_events=True, key='calligraphy', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12)),
           sg.Button('音楽部', size=(25, 2), enable_events=True, key='music', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12)),
           sg.Button('華道部', size=(25, 2), enable_events=True, key='flower-arrangement', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12))
       ],
           [
           sg.Button('化学部', size=(25, 2), enable_events=True, key='chemistry', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12)),
           sg.Button('茶道部', size=(25, 2), enable_events=True, key='tea-ceremony', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12)),
           sg.Button('物理部', size=(25, 2), enable_events=True, key='phisics', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12))
       ],
           [
           sg.Button('文芸部', size=(25, 2), enable_events=True, key='literature', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12)),
           sg.Button('生物部', size=(25, 2), enable_events=True, key='biology', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12)),
           sg.Button('ESS部', size=(25, 2), enable_events=True, key='ESS', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12))
       ],
           [
           sg.Button('天文部', size=(25, 2), enable_events=True, key='astronomy', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12)),
           sg.Button('家庭科研究部', size=(25, 2), enable_events=True, key='home-economics', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12)),
           sg.Button('囲碁将棋部', size=(25, 2), enable_events=True, key='go-shogi', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12))
       ],
           [
           sg.Button('美術部', size=(25, 2), enable_events=True, key='art', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12)),
           sg.Button('ビジネスライセンス部', size=(25, 2), enable_events=True, key='bussiness-license', button_color=('#ffd700', '#008080'), font=('UD デジタル 教科書体 N-R', 12))
       ],
            [
            sg.Button('メニュー画面に戻る', size=(20, 1), enable_events=True, key='back', button_color=('#ffd700', '#008080'), pad=((500, 0),(10,3)), font=('UD デジタル 教科書体 N-R', 10))
        ]
    ]
    return sg.Window('各部活動',each_club_layout, resizable=True)














def path_menu():
    path_layout = [
            [
            sg.Text('進路実績ページの編集及び更新', font=('UD デジタル 教科書体 N-R', 15), pad=((14, 14),(10,0)))
        ],
            [
            sg.Button('編集', size=(15, 1), enable_events=True, key='edit', button_color=('#ffd700', '#008080'), pad=((15, 15),(5,0)), font=('UD デジタル 教科書体 N-R', 12)),
            sg.Button('更新', size=(15, 1), enable_events=True, key='path-update', button_color=('#ffd700', '#008080'), pad=((15, 15),(5,0)), font=('UD デジタル 教科書体 N-R', 12))
        ],
            [
            sg.Button('メニュー画面に戻る', size=(20, 1), enable_events=True, key='back', button_color=('#ffd700', '#008080'), pad=((170, 0),(80,3)), font=('UD デジタル 教科書体 N-R', 10))
        ]

    ]
    return sg.Window('進路実績', path_layout)


def archive_menu():
    archive_layout = [
            [
            sg.Text('アーカイブ', font=('UD デジタル 教科書体 N-R', 15), pad=((160, 160),(10,0)))
        ],
            [
            sg.Text('毎年、年の最後に1度だけ作動させてください。', font=('UD デジタル 教科書体 N-R', 10))
        ],
            [
            sg.Button('アーカイブの保存', size=(45, 1), enable_events=True, key='archive-save', button_color=('#ffd700', '#008080'), pad=((26, 26),(5,20)), font=('UD デジタル 教科書体 N-R', 12))
        ],
            [
            sg.Text('進捗状況', font=('UD デジタル 教科書体 N-R', 10))
        ],
            [
            sg.ProgressBar(BAR_MAX, orientation='h', size=(41, 20), key='progress')
        ],
            [
            sg.Text('※ アーカイブの保存が終了すると、自動で別ウィンドウが開きます。', font=('UD デジタル 教科書体 N-R', 10))
        ],
            [
            sg.Button('メニュー画面に戻る', size=(20, 1), enable_events=True, key='back', button_color=('#ffd700', '#008080'), pad=((270, 0),(80,3)), font=('UD デジタル 教科書体 N-R', 10))
        ]

    ]
    return sg.Window('蜻蛉の軌跡',archive_layout)


def archive_edit_menu():
    archive_edit_layout = [
            [
            sg.Text('アーカイブページの編集及び更新', font=('UD デジタル 教科書体 N-R', 15), pad=((33, 33),(10,0)))
        ],
            [
            sg.Text('カード要素に埋め込むリンク', font=('UD デジタル 教科書体 N-R', 10))
        ],
            [
            sg.Text('https://myxogastria0808.github.io/' + now.strftime('%Y') + '/', font=('UD デジタル 教科書体 N-R', 10), enable_events=True, key='archive-url')
        ],
            [
            sg.Text('※ URLをクリックするとクリップボードにコピーされます。', font=('UD デジタル 教科書体 N-R', 10))
        ],
            [
            sg.Button('編集', size=(15, 1), enable_events=True, key='edit', button_color=('#ffd700', '#008080'), pad=((50, 15),(5,0)), font=('UD デジタル 教科書体 N-R', 12)),
            sg.Button('更新', size=(15, 1), enable_events=True, key='archive-update', button_color=('#ffd700', '#008080'), pad=((15, 50),(5,0)), font=('UD デジタル 教科書体 N-R', 12))
        ],
            [
            sg.Text('誤ってアーカイブの保存をしてしまった場合', font=('UD デジタル 教科書体 N-R', 12), pad=((0, 0),(60,0)))
        ],
            [
            sg.Text('アーカイブの削除ボタンを押してください。', font=('UD デジタル 教科書体 N-R', 10))
        ],
            [
            sg.Text('※ アーカイブの削除ボタンを押すと、管理者ページが開きます。', font=('UD デジタル 教科書体 N-R', 10))
        ],
            [
            sg.Button('アーカイブの削除', size=(20, 1), enable_events=True, key='archive-delete', button_color=('#ffd700', '#008080'), pad=((120, 120),(5,0)), font=('UD デジタル 教科書体 N-R', 10))
        ],
            [
            sg.Button('メニュー画面に戻る', size=(20, 1), enable_events=True, key='back', button_color=('#ffd700', '#008080'), pad=((240, 0),(80,3)), font=('UD デジタル 教科書体 N-R', 10))
        ]
    ]
    return sg.Window('蜻蛉の軌跡', archive_edit_layout)


def admin_menu():
    admin_layout = [
            [
            sg.Text('ウェブサイトの編集及び更新', font=('UD デジタル 教科書体 N-R', 15), pad=((130, 130),(20,0)), text_color=('#4ec994'))
        ],
            [
            sg.Button('編集', size=(20, 1), enable_events=True, key='edit', button_color=('#fff', '#daa520'), pad=((80, 15),(5,0)), font=('UD デジタル 教科書体 N-R', 12)),
            sg.Button('更新', size=(20, 1), enable_events=True, key='admin-update', button_color=('#fff', '#daa520'), pad=((15, 80),(5,0)), font=('UD デジタル 教科書体 N-R', 12))
        ],
            [
            sg.Text('※ 管理者メニューでは、全ファイルの編集・更新が行えます。', font=('UD デジタル 教科書体 N-R', 10), text_color=('#4ec994'))
        ],
            [
            sg.Text('GitHub', font=('UD デジタル 教科書体 N-R', 15), pad=((230, 230),(10,0)), text_color=('#4ec994'))
        ],
            [
            sg.Button('GitHub', size=(20, 1), enable_events=True, key='daily-img', button_color=('#fff', '#daa520'), pad=((178, 178),(2,0)), font=('UD デジタル 教科書体 N-R', 12))
        ],
            [
            sg.Text('※ GitHubボタンを押すとウェブサイトを管理しているGitHubのサイトが表示されます。', font=('UD デジタル 教科書体 N-R', 10), text_color=('#4ec994'))
        ],
            [
            sg.Text('アーカイブの削除', font=('UD デジタル 教科書体 N-R', 15), pad=((177, 177),(20,0)), text_color=('#4ec994'))
        ],
            [
            sg.Button('アーカイブの削除', size=(20, 1), enable_events=True, key='daily-img', button_color=('#fff', '#daa520'), pad=((178, 178),(2,0)), font=('UD デジタル 教科書体 N-R', 12))
        ],
            [
            sg.Button('メニュー画面に戻る', size=(20, 1), enable_events=True, key='back', button_color=('#fff', '#daa520'), pad=((375, 0),(80,3)), font=('UD デジタル 教科書体 N-R', 10))
        ]
    ]
    return sg.Window('Daily Life', admin_layout)


def archive_login_menu():
    archive_login_layout = [
           [
           sg.Text('password', font=('UD デジタル 教科書体 N-R', 12), pad=((0, 5),(10,0))),
           sg.InputText(size=(25, 1), key="archive-input-password", pad=((5, 0),(10,0)))
        ],
           [
           sg.Button('ログイン', size=(15, 1), enable_events=True, key='archive-login', button_color=('#ffd700', '#008080'), pad=((0, 0),(10,0)), font=('UD デジタル 教科書体 N-R', 12))
        ],
            [
            sg.Button('戻る', size=(5, 1), enable_events=True, key='back', button_color=('#ffd700', '#008080'), pad=((210, 0),(10,0)), font=('UD デジタル 教科書体 N-R', 10))
        ]
    ]
    return sg.Window('ログイン画面', archive_login_layout)


def admin_login_menu():
    admin_login_layout = [
           [
           sg.Text('password', font=('UD デジタル 教科書体 N-R', 12), pad=((0, 5),(10,0))),
           sg.InputText(size=(25, 1), key="admin-input-password", pad=((5, 0),(10,0)))
        ],
           [
           sg.Button('ログイン', size=(15, 1), enable_events=True, key='admin-login', button_color=('#ffd700', '#008080'), pad=((0, 0),(10,0)), font=('UD デジタル 教科書体 N-R', 12))
        ],
            [
            sg.Button('戻る', size=(5, 1), enable_events=True, key='back', button_color=('#ffd700', '#008080'), pad=((210, 0),(10,0)), font=('UD デジタル 教科書体 N-R', 10))
        ]
    ]
    return sg.Window('ログイン画面', admin_login_layout)


window = main_menu()

while True:
  event, values = window.read()
  if event == sg.WIN_CLOSED:
    break
  elif event == 'back':
    window.close()
    window = main_menu()
  elif event == 'edit':
    os.chdir('system')
    subprocess.run("edit.cmd", shell=True)
    os.chdir('..')

#==========Daily Life==========#
  elif event == 'daily':
    window.close()
    window = daily_menu()
  elif event == 'daily-update':
    os.chdir('system')
    os.chdir('check')
    subprocess.run("clone.cmd", shell=True)
    os.chdir('..')
    os.chdir('..')
    check = filecmp.cmp('./system/TestOHS-reset/index.html', './system/check/TestOHS-reset/index.html')
    #TestOHS-mainに変える！
    if check == True:
        os.chdir('system')
        subprocess.run("delete.cmd", shell=True)
        subprocess.run("DailyLifePush.cmd", shell=True)
    else:
        sg.popup_ok('更新をブロックしました。\n更新を行うには、以下のことを行ってください。\n1. ウェブサイトのフォルダー群をダウンロードフォルダーから別のディレクトリに移してください。\n2. 再度、フォルダー群をダウンロードしてください。\n3. 新しくダウンロードした方のフォルダー群で必要な編集を行ってください。\n4. 新しくダウンロードした方のフォルダー群を更新してください。\n--終了--')


#==========Announcement==========#
  elif event == 'announcement':
    window.close()
    window = announcement_menu()

#==========奨学金==========#
  elif event == 'schoolarship':
    window.close()
    window = schoolarship_menu()

#==========Calender==========#
  elif event == 'calender':
    window.close()
    window = calender_menu()

#==========学校紹介==========#
  elif event == 'introduction':
    window.close()
    window = introduction_menu()

#==========図書館==========#
  elif event == 'library':
    window.close()
    window = library_menu()

#==========食堂営業==========#
  elif event == 'cafeteria':
    window.close()
    window = cafeteria_menu()

#==========事務連絡==========#
  elif event == 'communication':
    window.close()
    window = communication_menu()

#==========部活動==========#
  elif event == 'club':
    window.close()
    window = club_menu()

  elif event == 'club-hub-page':
    window.close()
    window = club_hub_page()
  elif event == 'each-club':
    window.close()
    window = each_club()

#==========各部活動==========#







#==========進路実績==========#
  elif event == 'path':
    window.close()
    window = path_menu()

#==========蜻蛉の軌跡==========#
  elif event == 'archive':
    window.close()
    window = archive_login_menu()
  elif event == 'archive-save':
    subprocess.run("A.bat", shell=True)
    window['progress'].update(20)
    subprocess.run("B.bat", shell=True)
    window['progress'].update(40)
    subprocess.run("C.bat", shell=True)
    window['progress'].update(60)
    subprocess.run("D.bat", shell=True)
    window['progress'].update(80)
    subprocess.run("E.bat", shell=True)
    window['progress'].update(100)
    window.close()
    window = archive_edit_menu()
  elif event == 'archive-url':
    pyperclip.copy('https://myxogastria0808.github.io/' + now.strftime('%Y') + '/')
  elif event == 'archive-login':
    password = values['archive-input-password']
    if password == 'Hello': #<-passwordの設定は、Hello
        window.close()
        window = archive_menu()
    else:
        sg.popup_ok('パスワードが間違っています。')

#==========進路実績==========#
  elif event == 'admin':
    window.close()
    window = admin_login_menu()
  elif event == 'admin-login':
    password = values['admin-input-password']
    if password == 'Hello': #<-passwordの設定は、Hello
        window.close()
        window = admin_menu()
    else:
        sg.popup_ok('パスワードが間違っています。')



window.close()