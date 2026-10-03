---
id: software.testes.tranche16.001037
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

# Prism: validar requisição contra o contrato

## Em uma frase
Na função de proxy, requisições que não respeitam o contrato são reportadas e podem ser rejeitadas com resposta de erro estruturada.

## Por que importa
Contratos só geram valor quando a divergência aparece cedo, e a validação em tráfego real expõe incompatibilidades entre cliente e documentação.

## Como funciona
Ative a validação durante o desenvolvimento, acompanhe os relatórios e use o modo de erro estrito para interromper chamadas inválidas.

## Exemplo
Um campo obrigatório ausente enviado por engano pelo consumidor pode ser detectado imediatamente em vez de virar defeito em produção.

## Limites e trade-offs
Validação estrita pode bloquear tráfego legítimo quando o contrato está impreciso, e o relatório exige leitura para separar problema do documento de problema do cliente.

## Como verificar
Envie uma requisição inválida de propósito e confirme a resposta de erro estruturada e o cabeçalho que acompanha a violação.

## Conexões
- [[prism-prefer-header]] — Veja também: Prism: negociar respostas pelo cabeçalho de preferência.
- [[prism-proxy-mode]] — Veja também: Prism: intermediar serviço real com contrato.

## Fontes
- [Prism — HTTP mocking](https://docs.stoplight.io/docs/prism/83dbbd75532cf-http-mocking) — modos estático e dinâmico, cabeçalho Prefer e respostas de violação; consultado em 2026-10-03.
- [Prism — CLI](https://docs.stoplight.io/docs/prism/beeaad4dc0227-prism-cli) — instalação, subcomandos mock e proxy e opções de validação; consultado em 2026-10-03.
