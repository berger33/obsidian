---
id: software.seguranca.tranche20.001914
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-20.md"
fontes: ["https://theupdateframework.io/docs/metadata/", "https://github.com/theupdateframework/specification/blob/master/tuf-spec.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# The Update Framework (TUF): Detectar freeze com expiração

## Em uma frase
**The Update Framework (TUF) — Detectar freeze com expiração:** Campos de expiração limitam por quanto tempo metadados podem ser aceitos sem atualização.

## Por que importa
O recorte de **detectar freeze com expiração** ajuda a proteger clientes de atualização com papéis de metadados separados, hashes, versões e limites de assinatura. A equipe registra risco, evidência e responsável.

## Como funciona
Para **detectar freeze com expiração**, clientes verificam Root, Timestamp, Snapshot e Targets segundo limiares, hashes, versões e expirações definidos. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Defina datas e processo operacional de renovação para metadados de teste. Teste em staging autorizado.

## Limites e trade-offs
Expiração curta pode causar indisponibilidade se publicação de metadados atrasar. Exceções exigem responsável e prazo.

## Como verificar
Simule metadado expirado e verifique recusa e alerta de operação. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[tuf-verificar-hashes-de-targets]] — Complementa o tópico com the update framework (tuf): verificar hashes de targets.

## Fontes
- [TUF — Metadata](https://theupdateframework.io/docs/metadata/) — documentação oficial de papéis, metadados, assinaturas, hashes e expiração; consultado em 2026-10-04.
- [TUF — Specification](https://github.com/theupdateframework/specification/blob/master/tuf-spec.md) — especificação oficial de protocolo e verificação de atualizações; consultado em 2026-10-04.
