## https://stackoverflow.com/questions/58004348/vis-jshow-to-use-storepositions  --- here explained how I got X, Y positions of node from vis.js output
import pandas as pd
import numpy as np 
import networkx as nx
from bokeh.io import show, save, output_file
from bokeh.models import Range1d, Circle, MultiLine, EdgesAndLinkedNodes , NodesAndLinkedEdges , TapTool, HoverTool
from bokeh.plotting import figure
from bokeh.plotting import from_networkx
from bokeh.models import CustomJS, Select, MultiChoice, Button
from bokeh.layouts import column, gridplot
import copy
from bokeh.models import EdgesAndLinkedNodes , EdgesAndLinkedNodes


node_positions = pd.read_pickle('industry_node_new_katon_kato_2_added.pkl')

#node attributes 
pos = node_positions.set_index('id')['coordinates'].to_dict()
node_group = node_positions.set_index('id')['group'].to_dict()
node_color = node_positions.set_index('id')['color'].to_dict()
node_name = node_positions.set_index('id')['label_x'].to_dict()
node_oked_code = node_positions.set_index('id')['label_y'].to_dict()
node_regions_final = node_positions.set_index('id')['all_kato'].to_dict()
size = node_positions.set_index('id')['size_bokeh'].to_dict()
list_of_oked = node_positions.oked.sort_values().astype(str).unique().tolist()
#node_pci = node_positions.set_index('label')['pci'].to_dict()
node_emp = node_positions.set_index('id')['industry_total'].to_dict()
#node_government_present = node_positions.set_index('label')['government'].to_dict()
# create a network
data = pd.read_pickle(r"ind_space_edges.pkl")
data = data.astype({'source': int, 'target':int})
G = nx.from_pandas_edgelist(data, edge_attr=True)


# set attributes 
nx.set_node_attributes(G, node_group , 'group')
nx.set_node_attributes(G, node_color , 'color')
nx.set_node_attributes(G, node_name , 'name')
nx.set_node_attributes(G, node_oked_code , 'oked_code')
nx.set_node_attributes(G,node_regions_final, 'regions' )
nx.set_node_attributes(G, size, 'size')
#nx.set_node_attributes(G, node_pci, 'pci')
nx.set_node_attributes(G, node_emp, 'Employment')
#nx.set_node_attributes(G, node_government_present, 'government')

list_of_regions = [('all', 'Все'),
('11', 'Акмолинская область'),
    ('1132', 'Акмолинская область, Аккольский район'),
 ('1134', 'Акмолинская область, Аршалынский район'),
 ('1136', 'Акмолинская область, Астраханский район'),
 ('1138', 'Акмолинская область, Атбасарский район'),
 ('1140', 'Акмолинская область, Буландынский район'),
 ('1170', 'Акмолинская область, Бурабайский район'),
 ('1144', 'Акмолинская область, Егиндыкольский район'),
 ('1146', 'Акмолинская область, Ерейментауский район'),
 ('1148', 'Акмолинская область, Есильский район'),
 ('1152', 'Акмолинская область, Жаксынский район'),
 ('1154', 'Акмолинская область, Жаркаинский район'),
 ('1156', 'Акмолинская область, Зерендинский район'),
 ('1110', 'Акмолинская область, Кокшетау Г.А.'),
 ('1160', 'Акмолинская область, Коргалжынский район'),
 ('1116', 'Акмолинская область, Косшы Г.А.'),
 ('1164', 'Акмолинская область, Сандыктауский район'),
 ('1118', 'Акмолинская область, Степногорск Г.А.'),
 ('1166', 'Акмолинская область, Целиноградский район'),
 ('1168', 'Акмолинская область, Шортандинский район'),
 ('1145', 'Акмолинская область, район Биржан сал'),
 ('15', 'Актюбинская область'),
 ('1534', 'Актюбинская область, Айтекебийский район'),
 ('1510', 'Актюбинская область, Актобе Г.А.'),
 ('1532', 'Актюбинская область, Алгинский район'),
 ('1536', 'Актюбинская область, Байганинский район'),
 ('1568', 'Актюбинская область, Иргизский район'),
 ('1540', 'Актюбинская область, Каргалинский район'),
 ('1546', 'Актюбинская область, Мартукский район'),
 ('1548', 'Актюбинская область, Мугалжарский район'),
 ('1556', 'Актюбинская область, Темирский район'),
 ('1552', 'Актюбинская область, Уилский район'),
 ('1542', 'Актюбинская область, Хобдинский район'),
 ('1560', 'Актюбинская область, Хромтауский район'),
 ('1564', 'Актюбинская область, Шалкарский район'),
 ('19', 'Алматинская область'),
 ('1936', 'Алматинская область, Балхашский район'),
 ('1940', 'Алматинская область, Енбекшиказахский район'),
 ('1942', 'Алматинская область, Жамбылский район'),
 ('1968', 'Алматинская область, Илийский район'),
 ('1952', 'Алматинская область, Карасайский район'),
 ('1944', 'Алматинская область, Кегенский район'),
 ('1958', 'Алматинская область, Райымбекский район'),
 ('1962', 'Алматинская область, Талгарский район'),
 ('1966', 'Алматинская область, Уйгурский район'),
 ('1910', 'Алматинская область, Қонаев Г.А.'),
 ('23', 'Атырауская область'),
 ('2310', 'Атырауская область, Атырау Г.А.'),
 ('2336', 'Атырауская область, Жылыойский район'),
 ('2340', 'Атырауская область, Индерский район'),
 ('2342', 'Атырауская область, Исатайский район'),
 ('2348', 'Атырауская область, Кзылкогинский район'),
 ('2346', 'Атырауская область, Курмангазинский район'),
 ('2352', 'Атырауская область, Макатский район'),
 ('2356', 'Атырауская область, Махамбетский район'),
 ('63', 'Восточно-Казахстанская область'),
 ('6340', 'Восточно-Казахстанская область, Глубоковский район'),
 ('6346', 'Восточно-Казахстанская область, Зайсанский район'),
 ('6354', 'Восточно-Казахстанская область, Катон-Карагайский район'),
 ('6352', 'Восточно-Казахстанская область, Курчумский район'),
 ('6324', 'Восточно-Казахстанская область, Риддер Г.А.'),
 ('6358', 'Восточно-Казахстанская область, Тарбагатайский район'),
 ('6362', 'Восточно-Казахстанская область, Уланский район'),
 ('6310', 'Восточно-Казахстанская область, Усть-Каменогорск Г.А.'),
 ('6368', 'Восточно-Казахстанская область, Шемонаихинский район'),
 ('6348', 'Восточно-Казахстанская область, район Алтай'),
 ('6356', 'Восточно-Казахстанская область, район Самар'),
 ('6354_2','Восточно-Казахстанская область, Катон-Карагайский район новый' ),
 ('31', 'Жамбылская область'),
 ('3136', 'Жамбылская область, Байзакский район'),
 ('3140', 'Жамбылская область, Жамбылский район'),
 ('3142', 'Жамбылская область, Жуалынский район'),
 ('3148', 'Жамбылская область, Кордайский район'),
 ('3154', 'Жамбылская область, Меркенский район'),
 ('3156', 'Жамбылская область, Мойынкумский район'),
 ('3160', 'Жамбылская область, Сарысуский район'),
 ('3162', 'Жамбылская область, Таласский район'),
 ('3110', 'Жамбылская область, Тараз Г.А.'),
 ('3166', 'Жамбылская область, Шуский район'),
 ('3150', 'Жамбылская область, район Турара Рыскулова'),
 ('27', 'Западно-Казахстанская область'),
 ('2732', 'Западно-Казахстанская область, Акжаикский район'),
 ('2754', 'Западно-Казахстанская область, Бокейординский район'),
 ('2736', 'Западно-Казахстанская область, Бурлинский район'),
 ('2740', 'Западно-Казахстанская область, Жангалинский район'),
 ('2742', 'Западно-Казахстанская область, Жанибекский район'),
 ('2748', 'Западно-Казахстанская область, Казталовский район'),
 ('2750', 'Западно-Казахстанская область, Каратобинский район'),
 ('2758', 'Западно-Казахстанская область, Сырымский район'),
 ('2760', 'Западно-Казахстанская область, Таскалинский район'),
 ('2762', 'Западно-Казахстанская область, Теректинский район'),
 ('2710', 'Западно-Казахстанская область, Уральск Г.А.'),
 ('2766', 'Западно-Казахстанская область, Чингирлауский район'),
 ('2744', 'Западно-Казахстанская область, район Бәйтерек'),
 ('35', 'Карагандинская область'),
 ('3532', 'Карагандинская область, Абайский район'),
 ('3536', 'Карагандинская область, Актогайский район'),
 ('3516', 'Карагандинская область, Балхаш Г.А.'),
 ('3540', 'Карагандинская область, Бухар-Жырауский район'),
 ('3510', 'Карагандинская область, Караганда Г.А.'),
 ('3548', 'Карагандинская область, Каркаралинский район'),
 ('3552', 'Карагандинская область, Нуринский район'),
 ('3556', 'Карагандинская область, Осакаровский район'),
 ('3521', 'Карагандинская область, Приозерск Г.А.'),
 ('3522', 'Карагандинская область, Сарань Г.А.'),
 ('3524', 'Карагандинская область, Темиртау Г.А.'),
 ('3528', 'Карагандинская область, Шахтинск Г.А.'),
 ('3564', 'Карагандинская область, Шетский район'),
 ('39', 'Костанайская область'),
 ('3932', 'Костанайская область, Алтынсаринский район'),
 ('3934', 'Костанайская область, Амангельдинский район'),
 ('3916', 'Костанайская область, Аркалык Г.А.'),
 ('3936', 'Костанайская область, Аулиекольский район'),
 ('3940', 'Костанайская область, Денисовский район'),
 ('3942', 'Костанайская область, Жангельдинский район'),
 ('3944', 'Костанайская область, Житикаринский район'),
 ('3948', 'Костанайская область, Камыстинский район'),
 ('3950', 'Костанайская область, Карабалыкский район'),
 ('3952', 'Костанайская область, Карасуский район'),
 ('3910', 'Костанайская область, Костанай Г.А.'),
 ('3954', 'Костанайская область, Костанайский район'),
 ('3920', 'Костанайская область, Лисаковск Г.А.'),
 ('3956', 'Костанайская область, Мендыкаринский район'),
 ('3958', 'Костанайская область, Наурзумский район'),
 ('3924', 'Костанайская область, Рудный Г.А.'),
 ('3962', 'Костанайская область, Сарыкольский район'),
 ('3966', 'Костанайская область, Узункольский район'),
 ('3968', 'Костанайская область, Федоровский район'),
 ('3964', 'Костанайская область, район Беимбета Майлина'),
 ('43', 'Кызылординская область'),
 ('4332', 'Кызылординская область, Аральский район'),
 ('4319', 'Кызылординская область, Байконыр Г.А.'),
 ('4336', 'Кызылординская область, Жалагашский район'),
 ('4340', 'Кызылординская область, Жанакорганский район'),
 ('4344', 'Кызылординская область, Казалинский район'),
 ('4346', 'Кызылординская область, Кармакшинский район'),
 ('4310', 'Кызылординская область, Кызылорда Г.А.'),
 ('4348', 'Кызылординская область, Сырдарьинский район'),
 ('4352', 'Кызылординская область, Чиилийский район'),
 ('47', 'Мангистауская область'),
 ('4710', 'Мангистауская область, Актау Г.А.'),
 ('4736', 'Мангистауская область, Бейнеуский район'),
 ('4718', 'Мангистауская область, Жанаозен Г.А.'),
 ('4742', 'Мангистауская область, Каракиянский район'),
 ('4746', 'Мангистауская область, Мангистауский район'),
 ('4750', 'Мангистауская область, Мунайлинский район'),
 ('4752', 'Мангистауская область, Тупкараганский район'),
 ('55', 'Павлодарская область'),
 ('5516', 'Павлодарская область, Аксу Г.А.'),
 ('5532', 'Павлодарская область, Актогайский район'),
 ('5536', 'Павлодарская область, Баянаульский район'),
 ('5542', 'Павлодарская область, Железинский район'),
 ('5546', 'Павлодарская область, Иртышский район'),
 ('5556', 'Павлодарская область, Майский район'),
 ('5510', 'Павлодарская область, Павлодар Г.А.'),
 ('5560', 'Павлодарская область, Павлодарский район'),
 ('5564', 'Павлодарская область, Успенский район'),
 ('5568', 'Павлодарская область, Щербактинский район'),
 ('5522', 'Павлодарская область, Экибастуз Г.А.'),
 ('5552', 'Павлодарская область, район Аққулы'),
 ('5548', 'Павлодарская область, район Тереңкөл'),
 ('59', 'Северо-Казахстанская область'),
 ('5932', 'Северо-Казахстанская область, Айыртауский район'),
 ('5934', 'Северо-Казахстанская область, Акжарский район'),
 ('5958', 'Северо-Казахстанская область, Аккайынский район'),
 ('5942', 'Северо-Казахстанская область, Есильский район'),
 ('5946', 'Северо-Казахстанская область, Жамбылский район'),
 ('5950', 'Северо-Казахстанская область, Кызылжарский район'),
 ('5952', 'Северо-Казахстанская область, Мамлютский район'),
 ('5910', 'Северо-Казахстанская область, Петропавловск Г.А.'),
 ('5936', 'Северо-Казахстанская область, Район Магжана Жумабаева'),
 ('5956', 'Северо-Казахстанская область, Район Шал акына'),
 ('5966', 'Северо-Казахстанская область, Район им.Габита Мусрепова'),
 ('5960', 'Северо-Казахстанская область, Тайыншинский район'),
 ('5962', 'Северо-Казахстанская область, Тимирязевский район'),
 ('5964', 'Северо-Казахстанская область, Уалихановский район'),
 ('61', 'Туркестанская область'),
 ('6116', 'Туркестанская область, Арысь Г.А.'),
 ('6138', 'Туркестанская область, Жетисайский район'),
 ('6140', 'Туркестанская область, Казыгуртский район'),
 ('6139', 'Туркестанская область, Келесский район'),
 ('6120', 'Туркестанская область, Кентау Г.А.'),
 ('6144', 'Туркестанская область, Мактааральский район'),
 ('6146', 'Туркестанская область, Ордабасынский район'),
 ('6148', 'Туркестанская область, Отрарский район'),
 ('6152', 'Туркестанская область, Сайрамский район'),
 ('6154', 'Туркестанская область, Сарыагашский район'),
 ('6156', 'Туркестанская область, Сузакский район'),
 ('6158', 'Туркестанская область, Толебийский район'),
 ('6110', 'Туркестанская область, Туркестан Г.А.'),
 ('6160', 'Туркестанская область, Тюлькубасский район'),
 ('6164', 'Туркестанская область, Шардаринский район'),
 ('6136', 'Туркестанская область, район Байдибека'),
 ('6155', 'Туркестанская область, район Сауран'),
 ('75', 'г.Алматы'),
 ('7512', 'г.Алматы, Алатауский район'),
 ('7511', 'г.Алматы, Алмалинский район'),
 ('7513', 'г.Алматы, Ауэзовский район'),
 ('7514', 'г.Алматы, Бостандыкский район'),
 ('7515', 'г.Алматы, Жетысуский район'),
 ('7517', 'г.Алматы, Медеуский район'),
 ('7518', 'г.Алматы, Наурызбайский район'),
 ('7519', 'г.Алматы, Турксибский район'),
 ('71', 'г.Астана'),
 ('7111', 'г.Астана, район Алматы'),
 ('7114', 'г.Астана, район Байқоңыр'),
 ('7112', 'г.Астана, район Есиль'),
 ('7113', 'г.Астана, район Сарыарка'),
 ('79', 'г.Шымкент'),
 ('7911', 'г.Шымкент, Абайский район'),
 ('7913', 'г.Шымкент, Аль-Фарабийский район'),
 ('7915', 'г.Шымкент, Енбекшинский район'),
 ('7917', 'г.Шымкент, Каратауский район'),
 ('10', 'область Абай'),
 ('1032', 'область Абай, Абайский район'),
 ('1036', 'область Абай, Аягозский район'),
 ('1038', 'область Абай, Бескарагайский район'),
 ('1040', 'область Абай, Бородулихинский район'),
 ('1042', 'область Абай, Жарминский район'),
 ('1044', 'область Абай, Кокпектинский район'),
 ('1018', 'область Абай, Курчатов Г.А.'),
 ('1010', 'область Абай, Семей Г.А.'),
 ('1046', 'область Абай, Урджарский район'),
 ('1034', 'область Абай, район Ақсуат'),
 ('33', 'область Жетісу'),
 ('3332', 'область Жетісу, Аксуский район'),
 ('3334', 'область Жетісу, Алакольский район'),
 ('3336', 'область Жетісу, Ескельдинский район'),
 ('3344', 'область Жетісу, Каратальский район'),
 ('3340', 'область Жетісу, Кербулакский район'),
 ('3342', 'область Жетісу, Коксуский район'),
 ('3346', 'область Жетісу, Панфиловский район'),
 ('3348', 'область Жетісу, Саркандский район'),
 ('3310', 'область Жетісу, Талдыкорган Г.А.'),
 ('3318', 'область Жетісу, Текели Г.А.'),
 ('62', 'область Ұлытау'),
 ('6236', 'область Ұлытау, Жанааркинский район'),
 ('6210', 'область Ұлытау, Жезказган Г.А.'),
 ('6218', 'область Ұлытау, Каражал Г.А.'),
 ('6220', 'область Ұлытау, Сатпаев Г.А.'),
 ('6238', 'область Ұлытау, Улытауский район')]
 
 ## create a grand section selector.
list_of_grand_sections = [('all', 'Все'),
                          ('Сельское, лесное и рыбное хозяйство' , 'Сельское, лесное и рыбное хозяйство'),
                          ( 'Горнодобывающая промышленность и разработка карьеров', 'Горнодобывающая промышленность и разработка карьеров'),
                          ( 'Обрабатывающая промышленность', 'Обрабатывающая промышленность'),
                          ( 'Электроснабжение, подача газа, пара и воздушное  кондиционирование', 'Электроснабжение, подача газа, пара и воздушное  кондиционирование'),
                          ("Строительство","Строительство"),
                          ("Торговля" ,"Торговля" ),
                          ("Транспорт и складирование","Транспорт и складирование"),
                          ("Креативные услуги","Креативные услуги"),
                          ("Бизнес  услуги", "Бизнес  услуги"),
                          ("Локальные услуги","Локальные услуги"),
                          ('Государственные и социальные услуги','Государственные и социальные услуги')
]
## https://docs.bokeh.org/en/latest/docs/user_guide/topics/graph.html
## https://melaniewalsh.github.io/Intro-Cultural-Analytics/06-Network-Analysis/02-Making-Network-Viz-with-Bokeh.html

title = 'Пространство индустрий'

#Establish which categories will appear when hovering over each node
HOVER_TOOLTIPS = [("Название отрасли", "@name") , ('Группа' , '@group') , ('Условная занятость' , '@Employment') , ('ОКЭД' , '@oked_code') ]

#Create a plot — set dimensions, toolbar, and title
# tooltips = "name : @name , <br> group : @group, <br> pci : @pci, <br> Employment : @Employment",
plot = figure(
              tools="pan,wheel_zoom,save,reset", active_scroll='wheel_zoom',
            x_range=Range1d(-10000, 10000), y_range=Range1d(-5000, 5000), title=title , min_width=1500 )

#Create a network graph object with spring layout
# https://networkx.github.io/documentation/networkx-1.9/reference/generated/networkx.drawing.layout.spring_layout.html

plot.axis.visible = False

plot.add_tools(TapTool(), HoverTool(tooltips= HOVER_TOOLTIPS , attachment='vertical'))

network_graph = from_networkx(G, pos , scale=10, center=(0, 0))


# network_graph.layout_provider = StaticLayoutProvider(graph_layout=pos)

#Set node size and color
network_graph.node_renderer.glyph = Circle(size='size', fill_color='color')
network_graph.node_renderer.selection_glyph = Circle(size='size', fill_color='color', line_color="#5a5a5a")
network_graph.node_renderer.hover_glyph = Circle(size='size', fill_color='color', line_color="red" )

#Set edge opacity and width
network_graph.edge_renderer.glyph = MultiLine(line_alpha=0.2, line_width=1)

network_graph.edge_renderer.selection_glyph = MultiLine(line_color='black', line_width=1)

network_graph.edge_renderer.hover_glyph = MultiLine(line_color='red', line_width=1 , line_dash='dashed')


network_graph.selection_policy = NodesAndLinkedEdges()
network_graph.inspection_policy = NodesAndLinkedEdges()

#Add network graph to the plot
plot.renderers.append(network_graph)


initial_node_data = copy.deepcopy(network_graph.node_renderer.data_source.data) #this is list

# Select menu




select_grand_section = Select(title='Секция' , value="all", options=list_of_grand_sections, width=480)
multi_choice = MultiChoice(title="Выберите интересующие вас регионы",width=480,value=['all'],  options=list_of_regions, search_option_limit  = 100)
select = Select(title="Выбранные регионы", width=480, options=[['all', 'Все']] ,value="all" )
numeric_input_search = MultiChoice(title="Поиск индустрий в пространстве: Введите код ОКЭД (1111-96090)",width=480,  options=list_of_oked, search_option_limit  = 100)



multi_choice_callback =  CustomJS(args=dict(multi_choice=multi_choice, select=select), code="""
    // Get the selected values from MultiChoice
    var selectedValues = multi_choice.value;
    var optionsAll = multi_choice.options;
    
                                  
    var filteredOptions = optionsAll.filter(option => selectedValues.includes(option[0]));
    
    // Update the options of the Select widget with the selected values
    select.options = filteredOptions;
    // If "all" is not in the selected values, set the value of Select to the first selected value
    if (!selectedValues.includes("all")) {
        select.value =   selectedValues[0];
    } else {
        // If "all" is in the selected values, set the value of Select to "all"
        select.value = "all";
    }
    
""")
callback = CustomJS(args=dict(source=network_graph.node_renderer.data_source, node_data = initial_node_data,region_selected_1 = select, grand_section=select_grand_section), code="""
 
function get_region_color (region_code, regions_array ){
const region_selected = region_code;
const node_region = regions_array;
const initial_colors = node_data.color
var color = [];
node_region.forEach(function (value, i) {
    if (value.includes(region_selected)) {
        color.push(initial_colors[i])
    } else {
        color.push("#FFFFFF")
    }
    
}) ;
if (region_selected == "all"){
    color = initial_colors;
}
return color

}
const section_selected = grand_section.value;
const region_selected = region_selected_1.value;
const initial_colors = node_data.color;
//var def_color = "#d3d3d3"
//if (section_selected == "обработка"){
//def_color = "#FFFFFF"
//}
var region_filter = get_region_color(region_selected, source.data.regions)
var new_color = []
source.data.group.forEach(function(value, i) {
    if (value == section_selected  && region_filter[i] != "#FFFFFF"){
        new_color.push(initial_colors[i]);
    } else {
        new_color.push("#FFFFFF");
        
    }
})
source.data.color = new_color;
if (section_selected == "all" && region_selected=="all"){
source.data.color = initial_colors;
} else if (section_selected == "all" && region_selected !="all"){
    source.data.color = region_filter;
}
source.change.emit();
    

""")
grand_section_callback = CustomJS(args=dict(source = network_graph.node_renderer.data_source, node_data = initial_node_data, region_selected_1 = select, grand_section=select_grand_section), code="""


function get_region_color (region_code, regions_array ){
const region_selected = region_code;
const node_region = regions_array;
const initial_colors = node_data.color
var color = [];
node_region.forEach(function (value, i) {
    if (value.includes(region_selected)) {
        color.push(initial_colors[i])
    } else {
        color.push("#FFFFFF")
    }
    
}) ;
if (region_selected == "all"){
    color = initial_colors;
}
return color

}
const section_selected = grand_section.value;
const region_selected = region_selected_1.value;
const initial_colors = node_data.color;
//var def_color = "#d3d3d3"
//if (section_selected == "обработка"){
//def_color = "#FFFFFF"
//}
var region_filter = get_region_color(region_selected, source.data.regions)
var new_color = []
source.data.group.forEach(function(value, i) {
    if (value == section_selected  && region_filter[i] != "#FFFFFF"){
        new_color.push(initial_colors[i]);
    } else {
        new_color.push("#FFFFFF");
        
    }
})
source.data.color = new_color;
if (section_selected == "all" && region_selected=="all"){
source.data.color = initial_colors;
} else if (section_selected == "all" && region_selected !="all"){
    source.data.color = region_filter;
}
source.change.emit();


""")


searchCallback_new = CustomJS(args=dict(source=network_graph.node_renderer.data_source, node_data = initial_node_data, search_oked=numeric_input_search,  region_selected_1 = select, grand_section=select_grand_section) , code= """
const searched_oked = search_oked.value;
//console.log((searched_oked.length));
//console.log(node_data.color);
const initial_colors = node_data.color;
const section_selected = grand_section.value;
const region_selected = region_selected_1.value;
var colors_updated = [];
var i_int = 0


function get_region_color (region_code, regions_array ){
const region_selected = region_code;
const node_region = regions_array;
var color = [];
node_region.forEach(function (value, i) {
    if (value.includes(region_selected)) {
        color.push(initial_colors[i])
    } else {
        color.push("#FFFFFF")
    }
    
}) ;
if (region_selected == "all"){
    color = initial_colors;
}
return color

} 

if (searched_oked.length != 0) { 
    source.data.index.forEach(function(value, i) {
        for (const k in searched_oked){   
            i_int = Number(searched_oked[k]); 
            console.log(i_int); 
            if (value == i_int) {
                colors_updated.push(node_data.color[i]);
                console.log("success");
            } else{
                colors_updated.push("#FFFFFF");
            }
        }
    })
source.data.color = colors_updated;
source.change.emit();
} else {
    console.log(section_selected);
    console.log(region_selected);                      
    var region_filter = get_region_color(region_selected, source.data.regions)
    var new_color = []
    source.data.group.forEach(function(value, i) {
        if (value == section_selected  && region_filter[i] != "#FFFFFF"){
            new_color.push(initial_colors[i]);
        } else {
            new_color.push("#FFFFFF");
            
        }
    })
    source.data.color = new_color;
    if (section_selected == "all" && region_selected=="all"){
    source.data.color = initial_colors;
                             
    } else if (section_selected == "all" && region_selected !="all"){
        source.data.color = region_filter;
    }
    source.change.emit();

}




//var def_color = "#d3d3d3"
//if (section_selected == "обработка"){
//def_color = "#FFFFFF"
//}






""")


multi_choice.js_on_change("value", multi_choice_callback)
select.js_on_change("value", callback)
select_grand_section.js_on_change('value', grand_section_callback)
numeric_input_search.js_on_change("value", searchCallback_new)
## government okeds

# list_of_government = [('all', 'Выкл.'),
#                       ('9', 'Все гос.'),
#                           ('1' , 'Республиканская собс.'),
#                           ( '2', 'коммунальная собс.'),
#                           ( '3', 'более 50% респуб.'),
#                           ( '4', 'более 50% коммун.'),
#                           ("5","более 50% нац. комп."),
#                           ('0', 'Нету гос.')
# ]

# select_government = Select(title='Присуствует государство' , value="all", options=list_of_government)
# government_section_callback = CustomJS(args=dict(source = network_graph.node_renderer.data_source, node_data = initial_node_data, governement_type=select_government), code="""
# const government_selected = governement_type.value;
# console.log(source);
# const initial_colors = node_data.color;
# var new_color = []
# source.data.government.forEach(function(value, i) {
#     if ( value.includes(government_selected) ){
#         new_color.push(initial_colors[i])
#     } else { new_color.push('#FFFFFF')}
# })

# source.data.color = new_color;
# if (government_selected == "all") {
# source.data.color = initial_colors;
# }
# source.change.emit();
# """)
# select_government.js_on_change('value', government_section_callback)



#legend 
from bokeh.models import Div
legendEntries = {
    '#00B050': 'Сельхоз',
    '#000000': 'Добыча',
    '#a6a6a6': 'Обработка', 
    '#375fac': 'Энерго-, водоснабжение',
    '#933177': 'Строительство',
    '#ad85e4': 'Торговля',
    '#b9ede0': 'Транспорт и складирование',
    '#ffc000': 'Креативные услуги',
    '#fe0000': 'Бизнес  услуги',
    '#ff33a3': 'Локальные услуги',
    '#c55b11': 'Гос. и соц. сфера'
}

with open ("resources/legend.css", "r") as f:
    legend_css=f.read()

with open ("resources/legend.html", encoding='utf-8') as f:
    legend_html=f.read()

def str_legend():
    return "<p>" + "</p><p>".join([f"<span class='legend-entry' style='background:{n}'>&nbsp;</span>{v}" for n, v in legendEntries.items()]) + "</p>"

div_legend = Div(css_classes=["legend-container"],
    text=f"<style>{legend_css}</style>{legend_html.replace('<p></p>',str_legend())}")


div_description = Div(text=""" 
Ниже представлено пространство отраслей Казахстана, на основе реальных данных по районам и подклассам. <br>
Каждый <b>круг</b> - это подкласс, его <b>размер</b> - условная занятость, <b>цвет</b> - отрасль. <br>
Линии между кругами означают <b>наличие связи</b>, т. е. насколько 2 подкласса представлены в одних и тех же районах со специализацией. Для визуального удобства мы оставили только самые значимые связи. <br>
Исследуйте самостоятельно расположение торговли в пространстве, в разрезе районов.
""",
width=750)

button = Button(label="Очистить")

button_callback = CustomJS(args=dict(s=select, m = multi_choice, n= numeric_input_search, section =  select_grand_section ), code="""
                    m.value=['all' ]
                    s.value='all'
                    n.value = []
                    section.value='all'
                        
                    """)
button.js_on_event('button_click', button_callback)

#layout = column(select , select_grand_section,numeric_input,plot)
layout = gridplot([
    [ None,div_description],
    [div_legend, column(button,multi_choice, select , select_grand_section,numeric_input_search,plot)] 
    
    ])
output_file('industry_space_701_average.html')
show(layout)

