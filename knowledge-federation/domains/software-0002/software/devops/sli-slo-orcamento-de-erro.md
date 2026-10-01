---
id: software.devops.sli-slo-orcamento.000001
tipo: tecnica
dominio: software
subdominio: devops
nivel: intermediario
confianca: alta
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: pendente
revisor: ""
fontes: ["https://sre.google/workbook/slo-document/", "https://sre.google/workbook/alerting-on-slos/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
aliases: [SLI, SLO e orçamento de erro]
---

# SLI, SLO e orçamento de erro

## Em uma frase
Um SLI mede um aspecto observável do serviço, um SLO define o objetivo para esse indicador em uma janela, e o orçamento de erro quantifica a margem de falha compatível com o objetivo.

## Por que importa
“Disponibilidade alta” não é um critério operacional até que a equipe defina o que conta como sucesso, quem é afetado e em que período a medição ocorre. Indicadores e objetivos explícitos ajudam a discutir confiabilidade com base em impacto do usuário, em vez de escolher alertas pelo volume de eventos internos.

## Como funciona
Escolha um evento bom e um total representativo, por exemplo requisições válidas que completam com sucesso dividido pelo total de requisições válidas. Um SLO de 99,9% na janela acordada deixa 0,1% de eventos ruins dentro do orçamento; sobre um milhão de eventos elegíveis, isso corresponde a mil eventos. A equipe deve documentar filtros, janela, exclusões e fonte de dados. Alertas por taxa de consumo do orçamento (burn rate) procuram detectar degradação relevante sem paginar por toda oscilação curta.

## Exemplo
Para uma API de consulta, a equipe pode definir como evento bom uma resposta correta abaixo de um limite de latência. Um contador simples de respostas 2xx não mede correção nem lentidão. O SLI deve refletir a jornada que o cliente percebe; a regra de alerta e a política de release são decisões subsequentes, não propriedades automáticas do número.

## Limites e trade-offs
Um SLO mal escolhido incentiva otimização da métrica em vez do produto. Tráfego baixo torna taxas instáveis; dependências e regiões podem exigir segmentação. SLO não é sinônimo de SLA: um SLA pode criar compromissos contratuais, enquanto o SLO costuma orientar operação interna. O orçamento também não substitui análise de causa, segurança ou recuperação de desastre.

## Como verificar
Recalcule o SLI a partir de eventos amostrados e compare com dashboards. Teste janelas curtas e longas, baixo tráfego, erro completo e degradação parcial. Revise se cada página exige ação imediata e se falsos positivos/negativos são aceitáveis. Registre alterações de definição para manter comparabilidade temporal.

## Conexões
- [[observabilidade-sinais-distribuidos]] — fornece sinais para investigar mudanças no SLI.
- [[timeouts-retries-backoff-jitter]] — retries afetam carga, latência e erro percebido.
- [[gates-de-qualidade-no-merge]] — políticas de release podem responder ao risco operacional.

## Fontes
- [Google SRE Workbook — Example SLO Document](https://sre.google/workbook/slo-document/) — exemplo de definição, janela e orçamento; acesso em 2026-10-01.
- [Google SRE Workbook — Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/) — trade-offs de alertas por burn rate e janelas; acesso em 2026-10-01.
