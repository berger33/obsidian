---
id: software.testes.tranche22.001640
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://github.com/SpectoLabs/hoverfly/blob/master/README.md", "https://docs.hoverfly.io/en/latest/index.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Hoverfly: simulações de API num binário

## Em uma frase
O Hoverfly é uma ferramenta leve e open-source de simulação de APIs: substitui dependências lentas e instáveis por simulações realistas e reutilizáveis, com direito a latência de rede, falhas aleatórias e rate limits para exercitar casos extremos.

## Por que importa
Testes de integração morrem por serviços de terceiros — ambiente compartilhado, cota, instabilidade; simular o contrato no próprio job transforma suíte flaky em suíte determinística.

## Como funciona
O pacote traz CLI, bindings nativos (Java é o exemplo destacado) e REST API; as simulações são exportáveis, compartilháveis, editáveis e importáveis, e o projeto roda sob licença Apache 2, mantido pela iOCO Solutions.

## Exemplo
Os selos no topo do README oficial listam exatamente essa proposta em bullets, do "replace slow, flaky API dependencies" ao "run anywhere".

## Limites e trade-offs
Simular não é testar o serviço real: mudanças de contrato no terceiro só pegam num teste de contrato — o Hoverfly cobre o seu lado da conversa, não o dele.

## Como verificar
Abra a página inicial da doc e confirme que os bullets de proposta no site batem com o README do repositório.

## Conexões
- [[hoverfly-two-binaries]] — Veja também: Hoverfly: o par hoverfly + hoverctl.

## Fontes
- [Hoverfly — README oficial](https://github.com/SpectoLabs/hoverfly/blob/master/README.md) — proposta, quickstart, build em Go e contribuição; consultado em 2026-10-03.
- [Hoverfly — documentação inicial](https://docs.hoverfly.io/en/latest/index.html) — conceitos-chave, reference e troubleshooting do v1.12.15; consultado em 2026-10-03.
