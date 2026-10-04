---
id: software.testes.tranche12.000636
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://github.com/postmanlabs/newman/blob/develop/README.md", "https://github.com/postmanlabs/newman/blob/develop/README.md#api-reference"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Newman: distinguir timeout total, de request e de script

## Em uma frase
Newman configura limites distintos para duração da execução, requests e scripts, que protegem partes diferentes do workflow.

## Por que importa
Um único limite amplo pode deixar request travada consumir o job inteiro ou interromper uma collection legítima por causa de um script de setup lento.

## Como funciona
Meça o comportamento normal, configure as opções `--timeout`, `--timeout-request` e `--timeout-script` conforme a dependência correspondente e registre qual limite causou a falha.

## Exemplo
Um endpoint externo pode ter budget curto por request, enquanto o timeout total considera a sequência completa de dezenas de chamadas.

## Limites e trade-offs
Elevar todos os limites não corrige indisponibilidade e pode prolongar o feedback sem fornecer informação adicional sobre a operação presa.

## Como verificar
Provoque timeout em cada camada num ambiente controlado e confirme que o resumo identifica se o bloqueio ocorreu em script, request ou execução total.

## Conexões
- [[newman-bail-exit-status]] — Veja também: Newman: decidir entre interromper cedo e preservar diagnóstico.
- [[newman-reporters-artifacts]] — Veja também: Newman: combinar reporters sem perder saída CLI.

## Fontes
- [Newman — README e opções](https://github.com/postmanlabs/newman/blob/develop/README.md) — estado de manutenção, CLI, opções, reporters e uso como biblioteca; consultado em 2026-10-02.
- [Newman — API Reference](https://github.com/postmanlabs/newman/blob/develop/README.md#api-reference) — newman.run, eventos e callback de conclusão; consultado em 2026-10-02.
