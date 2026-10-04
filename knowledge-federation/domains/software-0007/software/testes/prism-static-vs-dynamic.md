---
id: software.testes.tranche16.001035
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://docs.stoplight.io/docs/prism/83dbbd75532cf-http-mocking", "https://docs.stoplight.io/docs/prism/beeaad4dc0227-prism-cli"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Prism: escolher entre exemplo e esquema

## Em uma frase
O modo predefinido responde com os exemplos declarados no contrato, enquanto o modo dinâmico gera valores a partir dos esquemas.

## Por que importa
Exemplos são estáveis e facilitam asserções; valores gerados cobrem variação de tipos e revelam fragilidade em consumidores que assumem conteúdo fixo.

## Como funciona
Use modo predefinido para demonstrações e testes determinísticos e modo dinâmico para verificar que o consumidor aceita dados variados.

## Exemplo
Um formulário alimentado por lista simulada pode ser testado primeiro com exemplos fixos e depois com valores gerados para revelar suposições.

## Limites e trade-offs
Valores aleatórios dificultam comparação entre execuções, e exemplos incompletos no contrato deixam campos sem representação.

## Como verificar
Execute a mesma rota nos dois modos e confirme que as asserções estáveis continuam passando no modo dinâmico.

## Conexões
- [[prism-mock-mode]] — Veja também: Prism: iniciar um servidor a partir da especificação.
- [[prism-prefer-header]] — Veja também: Prism: negociar respostas pelo cabeçalho de preferência.

## Fontes
- [Prism — HTTP mocking](https://docs.stoplight.io/docs/prism/83dbbd75532cf-http-mocking) — modos estático e dinâmico, cabeçalho Prefer e respostas de violação; consultado em 2026-10-03.
- [Prism — CLI](https://docs.stoplight.io/docs/prism/beeaad4dc0227-prism-cli) — instalação, subcomandos mock e proxy e opções de validação; consultado em 2026-10-03.
