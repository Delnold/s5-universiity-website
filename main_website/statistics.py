import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.ticker
from io import BytesIO
from django.http import HttpResponse

def generate_chart_favourite_champion(favorites: dict):
    champions = favorites["champions"]
    y_pos = range(len(champions))
    counts = [int(x) for x in favorites["count"]]
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.barh(y_pos, counts, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(champions)
    ax.invert_yaxis()
    ax.set_xlabel('quantity')
    ax.set_title('Champions as favourite')
    plt.subplots_adjust(bottom=0.3)

    locator = matplotlib.ticker.MultipleLocator(1)
    plt.gca().xaxis.set_major_locator(locator)
    formatter = matplotlib.ticker.StrMethodFormatter("{x:.0f}")
    plt.gca().xaxis.set_major_formatter(formatter)

    buffer = BytesIO()
    canvas = FigureCanvasAgg(fig)
    canvas.print_png(buffer)
    plt.close(fig)

    return HttpResponse(buffer.getvalue(), content_type='image/png')
def generate_chart_videos_champion(champion_videos: dict):
    champions = champion_videos["champions"]
    y_pos = range(len(champions))
    counts = [int(x) for x in champion_videos["videos_count"]]
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.barh(y_pos, counts, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(champions)
    ax.invert_yaxis()
    ax.set_xlabel('quantity')
    ax.set_title('Videos of Champions')
    plt.subplots_adjust(bottom=0.3)

    locator = matplotlib.ticker.MultipleLocator(1)
    plt.gca().xaxis.set_major_locator(locator)
    formatter = matplotlib.ticker.StrMethodFormatter("{x:.0f}")
    plt.gca().xaxis.set_major_formatter(formatter)

    buffer = BytesIO()
    canvas = FigureCanvasAgg(fig)
    canvas.print_png(buffer)
    plt.close(fig)

    return HttpResponse(buffer.getvalue(), content_type='image/png')
