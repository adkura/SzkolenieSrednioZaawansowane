projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for lp, (proj, lead, startday) in enumerate(zip(projects, leaders, dates), 1):
    print('{} - The leader of {} started {} is {}'.format(lp, proj, startday, lead))



