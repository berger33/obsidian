---
id: software.testes.test-estimation.000001
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-04.md"
fontes: ["https://astqb.org/5-1-test-planning/", "https://astqb.org/assets/documents/CTFL-4.0-Sample-Exam4-3-Answers.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Test effort estimation, Test estimation, Estimativa de esforço de teste]
lote: software-testes-2000-0001
---

# Estimativa de esforço de teste: métodos e incerteza

## Em uma frase
Estimativa de esforço prevê o trabalho necessário para alcançar objetivos de teste usando dados, julgamento especializado ou combinação dos dois, sempre com pressupostos e margem de erro.

## Por que importa
Estimativas ajudam a negociar prazo, recursos e escopo, mas uma estimativa pontual tratada como compromisso certo pode esconder riscos e criar falsa precisão. O syllabus ISTQB observa que estimar tarefas menores tende a ser mais preciso; tarefas grandes podem ser decompostas em partes menores antes de estimar.

## Como funciona
O CTFL descreve quatro técnicas: ratios baseados em dados de projetos semelhantes; extrapolação de medições iniciais, particularmente útil em ciclos iterativos; Wideband Delphi, em que especialistas estimam individualmente e discutem diferenças até convergir; e estimativa de três pontos. Nesta última, especialistas fornecem estimativa otimista `a`, mais provável `m` e pessimista `b`; uma forma comum calcula `E = (a + 4m + b) / 6` e `SD = (b - a) / 6`. Ratio e extrapolação são métricas-based; Delphi e três pontos são expert-based. WBS reduz uma tarefa grande em componentes estimáveis.

## Exemplo
Se uma tarefa de testes tem estimativas de 6, 9 e 18 horas, respectivamente otimista, mais provável e pessimista, então `E = (6 + 4×9 + 18) / 6 = 10` horas e `SD = (18 − 6) / 6 = 2` horas. O intervalo de 8–12 horas é uma interpretação baseada nessa dispersão, não uma garantia estatística de prazo nem substituto para declarar pressupostos.

## Limites e trade-offs
Histórico de projeto não é comparável automaticamente: domínio, automação, equipe, ambiente e critérios podem mudar. Especialistas podem compartilhar vieses; extrapolação cedo demais usa poucas observações. A fórmula de três pontos expressa uma técnica, não uma distribuição universal nem previsão exata.

## Como verificar
Registre unidade, escopo, pressupostos, técnica, dados de entrada e incerteza. Compare estimativa com esforço observado sem penalizar a equipe por desvios; use os erros para recalibrar futuros intervalos. Reestime se riscos, requisitos ou dependências mudarem materialmente.

## Conexões
- [[test-planning-objetivos-escopo-comunicacao]] — a estimativa informa recursos e cronograma do plano.
- [[risk-based-testing-priorizacao-risco]] — riscos podem alterar o esforço de teste necessário.
- [[test-progress-metrics-relatorios-conclusao]] — medições reais atualizam estimativas futuras.

## Fontes
- [ASTQB — ISTQB CTFL §5.1: Test Planning](https://astqb.org/5-1-test-planning/) — pressupostos, erro de estimativa, decomposição e técnicas; acesso em 2026-10-01.
- [ASTQB — CTFL v4.0 Sample Exam #4 Answers](https://astqb.org/assets/documents/CTFL-4.0-Sample-Exam4-3-Answers.pdf) — aplicação e cálculo da estimativa de três pontos; acesso em 2026-10-01.
