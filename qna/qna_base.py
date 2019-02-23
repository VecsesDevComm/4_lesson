import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

dark_red = (200, 0, 0)
dark_green = (0, 200, 0)
dark_blue = (0, 0, 200)

screen_size = (display_width, display_height)
screen = pygame.display.set_mode(screen_size)

clock = pygame.time.Clock()

free_sans_normal = pygame.font.Font("FreeSans.ttf", 14)
free_sans_medium = pygame.font.Font("FreeSans.ttf", 24)
free_sans_large = pygame.font.Font("FreeSans.ttf", 32)

def draw_text_button(x, y, w, h, text, clickable = True):
  m_point = pygame.mouse.get_pos()
  m_click = pygame.mouse.get_pressed()
  action_intent = False

  if clickable and pygame.Rect((x, y), (w, h)).collidepoint(m_point):
    pygame.draw.rect(screen, green, (x, y, w, h))
    if m_click[0] == 1:
      action_intent = True
  else:
    pygame.draw.rect(screen, dark_green, (x, y, w, h))

  text_surface = free_sans_normal.render(text, True, black)
  text_rect = text_surface.get_rect()
  text_rect.center = ( (x + w / 2), (y + h / 2) )

  screen.blit(text_surface, text_rect)

  return action_intent


def draw_text(x, y, font, text):
  text_surface = font.render(text, True, black)
  text_rect = text_surface.get_rect()
  text_rect.center = ( x, y )
  screen.blit(text_surface, text_rect)


def show_question(index):
  text = questions[index]
  draw_text(display_width / 2, 50, free_sans_medium, text)


def show_answers(index, guessed = False):
  correct = corrects[index]
  options = answers[index]
  option_a = options[0]
  option_b = options[1]

  if guessed:
    if correct == 'a':
      draw_text_button(20, 500, 760, 40, option_a, False)
    else:
      draw_text_button(20, 550, 760, 40, option_b, False)
  else:
    click_on_a = draw_text_button(20, 500, 760, 40, option_a)
    click_on_b = draw_text_button(20, 550, 760, 40, option_b)
    
    if click_on_a:
      pygame.event.post(pygame.event.Event(GUESS_A))
    elif click_on_b:
      pygame.event.post(pygame.event.Event(GUESS_B))


def show_winner():
  draw_text(display_width / 2, 100, free_sans_large, 'Correct!')


def show_looser():
  draw_text(display_width / 2, 100, free_sans_large, '#Noob')


def show_scores(scores):
  text = '{} Pont a griffendélnek'.format(scores)
  draw_text(display_width / 2, 100, free_sans_large, text)


def show_next_question_button():
  click_on = draw_text_button(20, 300, 760, 60, 'Következő kérdés')
  if click_on:
    pygame.event.post(pygame.event.Event(NEXT_Q_EVENT))


questions = [
]

answers = [
]

corrects = [
]

NEXT_Q_EVENT = pygame.USEREVENT + 1
GUESS_A = pygame.USEREVENT + 2
GUESS_B = pygame.USEREVENT + 3

def game_loop():
  game = {
    'paused': False,
    'winner': False,
    'looser': False,
    'game_over': False,
    'current_question': 0,
    'current_points': 0
  }

  def user_guessed(guess):
    game['paused'] = True
    pygame.time.set_timer(NEXT_Q_EVENT, 10000)
    
    if guess == corrects[game['current_question']]:
      game['current_points'] = game['current_points'] + 1
      game['winner'] = True
    else:
      game['looser'] = True

  def next_question():
    game['paused'] = False
    game['winner'] = False
    game['looser'] = False

    game['current_question'] += 1
    if game['current_question'] >= len(questions):
      game['game_over'] = True

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

    screen.fill(white)
    pygame.display.update()
    clock.tick(15)


game_loop()
