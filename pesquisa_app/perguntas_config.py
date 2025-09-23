# -*- coding: utf-8 -*-

PERGUNTAS = {
    "informacoes_pessoais": {
        "titulo": "Informações Pessoais",
        "campos": {
            "ano_entrada": {
                "texto": "Entrei na empresa no ano de:",
                "tipo": "number",
                "min_value": 2010,
                "obrigatorio": True
            },
            "periodo_entrada": {
                "texto": "Entrei na empresa no período de:",
                "tipo": "selectbox",
                "opcoes": ["", "1º Semestre", "2º Semestre"],
                "obrigatorio": True
            },
            "previsao_saida": {
                "texto": "Pretendo ficar quanto tempo na empresa?",
                "tipo": "selectbox",
                "opcoes": ["","6 meses a 1 ano", "1 ano a 1 ano e 6 meses", "2 anos","Mais de 2 anos"],
                "obrigatorio": True
            },
            "diretoria": {
                "texto": "Atualmente, minha diretoria é:",
                "tipo": "selectbox",
                "opcoes": ["","Comercial", "Gestão de Pessoas", "Operações", "Projetos"],
                "obrigatorio": True
            }
        }
    },
    "lideranca_e_gestao": {
        "titulo": "Liderança e Gestão",
        "campos": {
            "acessibilidade_diretor": {
                "texto": "Meu/Minha diretor(a) é acessível.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
            "contato_diretoria_executiva": {
                "texto": "Tenho contato suficiente com a Diretoria Executiva.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
            "comunicacao_diretoria": {
                "texto": "Os integrantes da minha diretoria se comunicam bem entre si.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
            "delegacao_tarefas": {
                "texto": "A delegação de tarefas na minha diretoria é satisfatória.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
            "voz_nas_decisoes": {
                "texto": "Meu/Minha diretor(a) ouve os assessores para tomar decisões.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
            "confianca_lideranca": {
                "texto": "Tenho confiança na minha liderança imediata (diretor/gerente).",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
            "feedback_construtivo": {
                "texto": "Meu gestor direto me fornece feedback claro e construtivo.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
            "preocupacao_pessoal_gestor": {
                "texto": "Sinto que meu gestor direto se preocupa comigo como pessoa.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
             "confianca_decisoes_lideranca_geral": {
                "texto": "Tenho confiança nas decisões tomadas pela liderança da empresa.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            }
        }
    },
    "satisfacao_e_orgulho": {
        "titulo": "Satisfação e Orgulho (eNPS)",
        "campos": {
            "satisfacao_geral": {
                "texto": "Estou satisfeito(a) com a IN Junior.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
            "sentimento_de_ser_ouvido": {
                "texto": "Sinto-me ouvido(a) dentro da empresa.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
            "orgulho_de_trabalhar": {
                "texto": "Sinto orgulho de trabalhar nesta empresa.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
             "orgulho_da_minha_atividade": {
                "texto": "Sinto orgulho da minha atividade nesta empresa.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
            "preocupacao_futuro_empresa": {
                "texto": "Eu me preocupo com o futuro desta empresa.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
            "satisfacao_estrutura_hierarquica": {
                "texto": "Estou satisfeito com a estrutura hierárquica (Diretoria e Assessores).",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
            "recomendaria_empresa": {
                "texto": "Eu recomendaria esta empresa como um ótimo lugar para um amigo trabalhar.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            }
        }
    },
    "ambiente_de_trabalho": {
        "titulo": "Ambiente de Trabalho",
        "campos": {
            "seguranca_assumir_riscos": {
                "texto": "Considero o ambiente seguro para assumir riscos perante a equipe.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
            "conforto_pedir_ajuda": {
                "texto": "Me sinto confortável em pedir ajuda aos membros desta equipe.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
            "sentimento_pertencimento": {
                "texto": "Sinto que pertenço ao time e que meus colegas e líderes me tratam como igual.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
            "respeito_e_cordialidade": {
                "texto": "Os membros da equipe se tratam com respeito e cordialidade.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
            "conforto_cometer_erros": {
                "texto": "Me sinto confortável em cometer erros, pois entendo que faz parte do processo e recebo apoio.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
            "sentimento_desconfortavel_discurso": {
                "texto": "Já me senti acuado(a) ou desconfortável com o discurso de um ou mais colegas.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
            "conforto_expressar_opiniao_divergente": {
                "texto": "Sinto-me confortável para expressar minha opinião, mesmo que divergente.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
            "seguranca_emprego": {
                "texto": "Meu emprego é seguro na empresa e não corro o risco de tomar strike sem motivo.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
             "relacionamento_colegas": {
                "texto": "O relacionamento com meus colegas de trabalho favorece a execução das minhas atividades.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
            "espirito_cooperacao_diretoria": {
                "texto": "Há um forte espírito de cooperação e ajuda mútua na minha diretoria.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
            "resolucao_conflitos_equipe": {
                "texto": "Os conflitos dentro da minha equipe são resolvidos de forma aberta e construtiva.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            }
        }
    },
    "cultura_e_bem_estar": {
        "titulo": "Cultura e Bem-Estar",
        "campos": {
             "preocupacao_bem_estar_empresa": {
                "texto": "A empresa se preocupa genuinamente com meu bem-estar físico e mental.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
             "valores_praticados_dia_a_dia": {
                "texto": "Os valores da empresa são praticados no dia a dia, e não apenas no discurso.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
             "responsabilidade_social_etica": {
                "texto": "A empresa demonstra responsabilidade social e ética em suas práticas.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
            "conforto_expressar_orientacao_sexual": {
                "texto": "Me sinto confortável para expressar minha orientação sexual.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
            "conforto_expressar_crencas_religiosas": {
                "texto": "Me sinto confortável para expressar minha(s) crença(s) ou descrença(s) religiosa(s).",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
            "conforto_expressar_conviccoes_politicas": {
                "texto": "Me sinto confortável para expressar minhas convicções políticas.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
        }
    },
    "desenvolvimento_e_carreira": {
        "titulo": "Desenvolvimento e Carreira",
        "campos": {
            "sucesso_carreira_vida_profissional": {
                "texto": "Considero que estou obtendo sucesso na minha carreira e na minha vida profissional.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
            "trabalho_reconhecido_familia": {
                "texto": "Considero que o meu trabalho é reconhecido e valorizado pela minha família.",
                "tipo": "slider",
                "min_value": 1, "max_value": 5, "obrigatorio": True
            },
        }
    },
     "feedback_aberto": {
        "titulo": "Feedback Aberto",
        "campos": {
            "pontos_positivos": {
                "texto": "Quais os principais pontos positivos que você destacaria?",
                "tipo": "text_area",
                "obrigatorio": False
            },
            "pontos_melhoria": {
                "texto": "Quais pontos você acha que podem ser melhorados?",
                "tipo": "text_area",
                "obrigatorio": False
            }
        }
    }
}