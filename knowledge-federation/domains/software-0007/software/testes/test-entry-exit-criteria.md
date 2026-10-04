---
id: software.testes.entry-exit-criteria.000001
tipo: conceito
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
fontes: ["https://astqb.org/5-1-test-planning/", "https://agilealliance.org/glossary/definition-of-done/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Entry criteria, Exit criteria, Definition of Ready, Definition of Done]
lote: software-testes-2000-0001
---

# Critérios de entrada e saída em atividades de teste

## Em uma frase
Critérios de entrada descrevem pré-condições para começar uma atividade; critérios de saída definem o que precisa ser alcançado para declará-la concluída.

## Por que importa
Iniciar testes sem build utilizável, dados ou ambiente pode tornar o trabalho mais lento, caro e arriscado. Encerrar sem evidência sobre objetivos e riscos deixa stakeholders sem base para decidir o próximo passo. Critérios definidos antes da execução tornam essas decisões verificáveis e evitam renegociá-las apenas para justificar um prazo.

## Como funciona
O syllabus ISTQB recomenda critérios de entrada e saída para cada nível de teste, ajustados aos objetivos daquele nível. Entrada pode exigir que recursos, build, ambiente ou dados estejam disponíveis. Saída pode exigir execução de cenários prioritários, cobertura acordada, análise de defeitos ou comunicação do risco residual. Não existe uma lista universal: critérios precisam ser mensuráveis e viáveis no contexto. Em Agile, uma Definition of Done é uma lista acordada para considerar um incremento concluído; ela pode incluir teste e deployability, mas não deve ser confundida automaticamente com todo o conjunto de critérios de fechamento de uma fase ou release.

## Exemplo
Antes de testar uma API de pagamento, a equipe pode exigir um build identificável, sandbox acessível e credenciais de teste. Para encerrar, pode exigir que os cenários de autorização e idempotência sejam executados, que defeitos críticos sejam triados e que limitações conhecidas sejam comunicadas. Se a data de saída chegar com um critério não atendido, o responsável decide com stakeholders se continua, reduz escopo ou aceita explicitamente o risco — não se deve registrar o critério como cumprido.

## Limites e trade-offs
Critérios rígidos podem bloquear trabalho útil quando uma pré-condição parcial permite testes exploratórios seguros; exceções devem ser explícitas. Critérios vagos como “qualidade suficiente” não orientam uma decisão. Exigir correção de todos os defeitos pode ser impraticável; um critério pode permitir defeitos conhecidos desde que sejam avaliados e aceitos pelos responsáveis apropriados.

## Como verificar
Defina critérios antes do início, vincule-os aos objetivos e riscos, determine evidência e responsável para cada item e registre exceções com justificativa. No fechamento, reporte o que foi atendido, não atendido e aceito, incluindo o risco remanescente.

## Conexões
- [[test-planning-objetivos-escopo-comunicacao]] — registra critérios junto a objetivos, recursos e cronograma.
- [[test-progress-metrics-relatorios-conclusao]] — coleta evidência para avaliar critérios de saída.

## Fontes
- [ASTQB — ISTQB CTFL §5.1: Test Planning](https://astqb.org/5-1-test-planning/) — distinção, finalidade e variação contextual dos critérios; acesso em 2026-10-01.
- [Agile Alliance — Definition of Done](https://agilealliance.org/glossary/definition-of-done/) — critério acordado para considerar um incremento concluído e armadilhas de listas excessivas ou tácitas; acesso em 2026-10-01.
