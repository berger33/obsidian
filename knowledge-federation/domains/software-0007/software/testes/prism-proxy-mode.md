---
id: software.testes.tranche16.001038
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
fontes: ["https://docs.stoplight.io/docs/prism/beeaad4dc0227-prism-cli", "https://docs.stoplight.io/docs/prism/83dbbd75532cf-http-mocking"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Prism: intermediar serviço real com contrato

## Em uma frase
O modo de intermediação encaminha requisições ao serviço real e pode comparar o tráfego com a especificação, mantendo o trânsito inalterado quando não há modo estrito.

## Por que importa
Comparar tráfego observado com o contrato revela divergências documentais sem exigir mudança no serviço nem no consumidor.

## Como funciona
Aponte o consumidor para o intermediário, registre as diferenças e use a validação apenas quando puder interromper chamadas inválidas com segurança.

## Exemplo
Rodar a suíte de integração através do intermediário produz lista de divergências entre o que o serviço responde e o que o contrato promete.

## Limites e trade-offs
A intermediação adiciona latência e ponto de falha na cadeia, então não deve ser usada em ambiente de produção nem em medição de desempenho.

## Como verificar
Faça uma chamada direta e outra pelo intermediário e compare respostas para confirmar que o tráfego é repassado sem alteração.

## Conexões
- [[prism-validation-errors]] — Veja também: Prism: validar requisição contra o contrato.
- [[prism-generated-errors]] — Veja também: Prism: entender as respostas de violação.

## Fontes
- [Prism — CLI](https://docs.stoplight.io/docs/prism/beeaad4dc0227-prism-cli) — instalação, subcomandos mock e proxy e opções de validação; consultado em 2026-10-03.
- [Prism — HTTP mocking](https://docs.stoplight.io/docs/prism/83dbbd75532cf-http-mocking) — modos estático e dinâmico, cabeçalho Prefer e respostas de violação; consultado em 2026-10-03.
