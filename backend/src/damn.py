import json
from datetime import datetime, timedelta
from typing import List, Dict, Any
import random

class SocialMediaPlanGenerator:
    def __init__(self):
        self.platforms = {
            'instagram': {
                'optimal_times': ['09:00', '12:00', '17:00', '20:00'],
                'max_daily_posts': 2,
                'hashtag_limit': 30,
                'video_length': (15, 60),
                'engagement_peak_days': ['Tuesday', 'Wednesday', 'Thursday']
            },
            'tiktok': {
                'optimal_times': ['06:00', '10:00', '16:00', '19:00'],
                'max_daily_posts': 3,
                'hashtag_limit': 10,
                'video_length': (15, 60),
                'engagement_peak_days': ['Monday', 'Tuesday', 'Friday']
            },
            'youtube_shorts': {
                'optimal_times': ['14:00', '18:00', '21:00'],
                'max_daily_posts': 1,
                'hashtag_limit': 15,
                'video_length': (15, 60),
                'engagement_peak_days': ['Saturday', 'Sunday', 'Wednesday']
            }
        }
        
        self.content_themes = {
            'learning_breakthrough': {
                'caption_templates': [
                    "Когда математика наконец 'щелкнула'! 🧠✨ {subject} {hashtags}",
                    "Этот момент озарения стоит тысячи слов! 💡 {subject} {hashtags}",
                    "Смотрите, как наши ученики побеждают сложные задачи! 💪 {subject} {hashtags}"
                ],
                'hashtags': ['#образование', '#математика', '#озарение', '#обучение', '#azgroup']
            },
            'student_engagement': {
                'caption_templates': [
                    "Активное участие - залог успеха! 🙋‍♀️ {subject} {hashtags}",
                    "Когда урок превращается в увлекательную дискуссию! 🗣️ {subject} {hashtags}",
                    "Наши ученики не боятся задавать вопросы! ❓ {subject} {hashtags}"
                ],
                'hashtags': ['#активноеобучение', '#ученики', '#вопросы', '#дискуссия', '#azgroup']
            },
            'teaching_methods': {
                'caption_templates': [
                    "Креативный подход к объяснению сложных тем! 🎨 {subject} {hashtags}",
                    "Как сделать урок незабываемым? 🎭 {subject} {hashtags}",
                    "Современные методы обучения в действии! 🚀 {subject} {hashtags}"
                ],
                'hashtags': ['#методыобучения', '#креатив', '#современноеобразование', '#azgroup']
            }
        }
    
    def generate_publication_plan(self, highlights: List[Dict], days_ahead: int = 14) -> Dict[str, Any]:
        """
        Generate a comprehensive publication plan for extracted highlights
        
        Args:
            highlights: List of highlight segments with metadata
            days_ahead: Number of days to plan ahead
        
        Returns:
            Comprehensive publication plan
        """
        publication_plan = {
            'plan_created': datetime.now().isoformat(),
            'planning_period': f"{days_ahead} days",
            'total_highlights': len(highlights),
            'platforms': {},
            'weekly_themes': self._generate_weekly_themes(),
            'content_calendar': self._create_content_calendar(highlights, days_ahead),
            'performance_tracking': self._setup_tracking_metrics(),
            'content_optimization': self._generate_optimization_suggestions(highlights)
        }
        
        # Generate platform-specific plans
        for platform in self.platforms.keys():
            publication_plan['platforms'][platform] = self._generate_platform_plan(
                highlights, platform, days_ahead
            )
        
        return publication_plan
    
    def _create_content_calendar(self, highlights: List[Dict], days_ahead: int) -> List[Dict]:
        """Create a day-by-day content calendar"""
        calendar = []
        start_date = datetime.now().date()
        
        # Distribute highlights across platforms and days
        highlight_queue = highlights.copy()
        random.shuffle(highlight_queue)
        
        for day_offset in range(days_ahead):
            current_date = start_date + timedelta(days=day_offset)
            day_name = current_date.strftime('%A')
            
            day_plan = {
                'date': current_date.isoformat(),
                'day_name': day_name,
                'posts': {},
                'total_posts': 0
            }
            
            # Schedule posts for each platform based on optimal days
            for platform, settings in self.platforms.items():
                if day_name in settings['engagement_peak_days'] and highlight_queue:
                    posts_for_today = min(
                        settings['max_daily_posts'],
                        len(highlight_queue),
                        2 if day_offset < 7 else 1  # More frequent posting in first week
                    )
                    
                    day_plan['posts'][platform] = []
                    
                    for _ in range(posts_for_today):
                        if highlight_queue:
                            highlight = highlight_queue.pop(0)
                            post_time = random.choice(settings['optimal_times'])
                            
                            post_plan = self._create_post_plan(highlight, platform, post_time)
                            day_plan['posts'][platform].append(post_plan)
                            day_plan['total_posts'] += 1
            
            calendar.append(day_plan)
        
        return calendar
    
    def _create_post_plan(self, highlight: Dict, platform: str, post_time: str) -> Dict:
        """Create detailed plan for individual post"""
        theme = highlight.get('segment_theme', 'learning_breakthrough')
        theme_key = self._map_theme_to_category(theme)
        
        # Generate caption
        template = random.choice(self.content_themes[theme_key]['caption_templates'])
        hashtags = ' '.join([f"#{tag}" for tag in self.content_themes[theme_key]['hashtags'][:10]])
        
        subject = highlight.get('subject', 'урок')
        caption = template.format(subject=subject, hashtags=hashtags)
        
        # Add platform-specific optimizations
        if platform == 'tiktok':
            caption += "\n\n#fyp #viral #education #russia"
        elif platform == 'instagram':
            caption += f"\n\n📚 Подписывайтесь на @azgroup_education"
        
        return {
            'highlight_id': highlight.get('id', ''),
            'timestamp': highlight.get('extended_segment', ''),
            'post_time': post_time,
            'caption': caption,
            'hashtags': hashtags.split(),
            'expected_length': f"{highlight.get('duration', 30)}s",
            'editing_notes': self._generate_editing_notes(highlight, platform),
            'engagement_strategy': self._generate_engagement_strategy(theme_key, platform)
        }
    
    def _generate_editing_notes(self, highlight: Dict, platform: str) -> List[str]:
        """Generate editing suggestions for the highlight"""
        notes = []
        
        # Platform-specific editing notes
        if platform == 'tiktok':
            notes.extend([
                "Добавить динамичные переходы",
                "Использовать текстовые оверлеи для ключевых моментов",
                "Добавить трендовую музыку (соблюдать авторские права)"
            ])
        elif platform == 'instagram':
            notes.extend([
                "Создать привлекательную обложку",
                "Добавить субтитры для accessibility",
                "Оптимизировать под вертикальный формат"
            ])
        
        # Content-specific notes
        if 'breakthrough' in highlight.get('segment_theme', ''):
            notes.append("Выделить момент озарения ученика")
        if 'engagement' in highlight.get('segment_theme', ''):
            notes.append("Показать взаимодействие учителя и ученика")
        
        return notes
    
    def _generate_engagement_strategy(self, theme: str, platform: str) -> Dict:
        """Generate engagement strategy for the post"""
        strategies = {
            'learning_breakthrough': {
                'call_to_action': "А какой ваш любимый предмет? 💭",
                'questions': ["Помните свой первый момент понимания математики?"],
                'interaction_hooks': ["Поставьте ❤️ если тоже любите математику!"]
            },
            'student_engagement': {
                'call_to_action': "Расскажите о своем опыте обучения! 📚",
                'questions': ["Какие вопросы вы не боитесь задавать?"],
                'interaction_hooks': ["Отметьте друга, который тоже активен на уроках!"]
            }
        }
        
        base_strategy = strategies.get(theme, strategies['learning_breakthrough'])
        
        return {
            'post_timing': 'Оптимальное время публикации',
            'engagement_tactics': base_strategy,
            'follow_up_actions': [
                "Отвечать на комментарии в первые 2 часа",
                "Лайкать комментарии подписчиков",
                "Делиться в Stories с дополнительным контентом"
            ]
        }
    
    def _generate_weekly_themes(self) -> Dict:
        """Generate weekly content themes"""
        return {
            'week_1': 'Математические открытия',
            'week_2': 'Активное обучение',
            'week_3': 'Креативные методы преподавания',
            'week_4': 'Успехи учеников'
        }
    
    def _setup_tracking_metrics(self) -> Dict:
        """Setup metrics for tracking content performance"""
        return {
            'kpis': {
                'reach': 'Охват аудитории',
                'engagement_rate': 'Уровень вовлеченности',
                'saves': 'Сохранения',
                'shares': 'Репосты',
                'comments': 'Комментарии',
                'profile_visits': 'Переходы в профиль'
            },
            'tracking_schedule': 'Еженедельный анализ',
            'optimization_triggers': [
                'Низкий охват (<1000 просмотров)',
                'Низкая вовлеченность (<3%)',
                'Отсутствие комментариев'
            ]
        }
    
    def _generate_optimization_suggestions(self, highlights: List[Dict]) -> List[str]:
        """Generate suggestions for content optimization"""
        return [
            "A/B тестировать время публикации",
            "Экспериментировать с разными хэштегами",
            "Анализировать наиболее успешные форматы",
            "Создавать серии из связанных highlights",
            "Использовать пользовательский контент",
            "Взаимодействовать с образовательными аккаунтами"
        ]
    
    def _map_theme_to_category(self, theme: str) -> str:
        """Map highlight theme to content category"""
        theme_lower = theme.lower()
        if 'breakthrough' in theme_lower or 'понимание' in theme_lower:
            return 'learning_breakthrough'
        elif 'engagement' in theme_lower or 'участие' in theme_lower:
            return 'student_engagement'
        else:
            return 'teaching_methods'
    
    def _generate_platform_plan(self, highlights: List[Dict], platform: str, days_ahead: int) -> Dict:
        """Generate detailed plan for specific platform"""
        return {
            'total_posts_planned': len([h for h in highlights if self._should_post_on_platform(h, platform)]),
            'optimal_posting_times': self.platforms[platform]['optimal_times'],
            'content_strategy': f"Стратегия контента для {platform}",
            'hashtag_strategy': self._generate_hashtag_strategy(platform),
            'expected_metrics': self._estimate_performance_metrics(platform, len(highlights))
        }
    
    def _should_post_on_platform(self, highlight: Dict, platform: str) -> bool:
        """Determine if highlight should be posted on specific platform"""
        # Simple logic - can be made more sophisticated
        duration = highlight.get('duration', 30)
        min_duration, max_duration = self.platforms[platform]['video_length']
        return min_duration <= duration <= max_duration
    
    def _generate_hashtag_strategy(self, platform: str) -> Dict:
        """Generate hashtag strategy for platform"""
        general_hashtags = ['#azgroup', '#образование', '#обучение', '#школа']
        
        platform_specific = {
            'instagram': ['#reels', '#education', '#learning', '#russia'],
            'tiktok': ['#fyp', '#viral', '#eduktok', '#russia'],
            'youtube_shorts': ['#shorts', '#education', '#learning']
        }
        
        return {
            'always_include': general_hashtags,
            'platform_specific': platform_specific.get(platform, []),
            'trending': 'Добавлять трендовые хэштеги еженедельно',
            'limit': self.platforms[platform]['hashtag_limit']
        }
    
    def _estimate_performance_metrics(self, platform: str, num_highlights: int) -> Dict:
        """Estimate expected performance metrics"""
        base_metrics = {
            'instagram': {'avg_views': 2000, 'engagement_rate': 0.05},
            'tiktok': {'avg_views': 5000, 'engagement_rate': 0.08},
            'youtube_shorts': {'avg_views': 3000, 'engagement_rate': 0.04}
        }
        
        platform_metrics = base_metrics.get(platform, base_metrics['instagram'])
        
        return {
            'estimated_total_views': platform_metrics['avg_views'] * num_highlights,
            'estimated_engagement_rate': platform_metrics['engagement_rate'],
            'estimated_new_followers': num_highlights * 10,
            'performance_benchmark': 'Сравнить с предыдущими месяцами'
        }

# Example usage
def generate_plan_for_highlights(highlights_data):
    """
    Example function showing how to use the plan generator
    
    highlights_data should be a list of dictionaries with highlight information
    """
    planner = SocialMediaPlanGenerator()
    
    # Example highlight data structure
    example_highlights = [
        {
            'id': 'highlight_1',
            'extended_segment': '10:15-11:00',
            'segment_theme': 'learning_breakthrough',
            'duration': 45,
            'subject': 'математика',
            'confidence': 0.85
        },
        # Add more highlights...
    ]
    
    plan = planner.generate_publication_plan(example_highlights, days_ahead=14)
    
    # Save plan to file
    with open('social_media_plan.json', 'w', encoding='utf-8') as f:
        json.dump(plan, f, ensure_ascii=False, indent=2)
    
    print("Publication plan generated successfully!")
    return plan

if __name__ == "__main__":
    # Test the system
    test_highlights = [
        {
            'id': 'highlight_1',
            'extended_segment': '10:15-11:00',
            'segment_theme': 'learning_breakthrough',
            'duration': 45,
            'subject': 'математика',
            'confidence': 0.85
        }
    ]
    
    plan = generate_plan_for_highlights(test_highlights)
    print(json.dumps(plan, ensure_ascii=False, indent=2))