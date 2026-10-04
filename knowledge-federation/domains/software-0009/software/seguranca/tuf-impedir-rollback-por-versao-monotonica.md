---
id: software.seguranca.tranche20.001913
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

# The Update Framework (TUF): Impedir rollback por versão monotônica

## Em uma frase
**The Update Framework (TUF) — Impedir rollback por versão monotônica:** Versões em metadados permitem que cliente detecte tentativa de servir estado anterior já visto.

## Por que importa
O recorte de **impedir rollback por versão monotônica** ajuda a proteger clientes de atualização com papéis de metadados separados, hashes, versões e limites de assinatura. A equipe registra risco, evidência e responsável.

## Como funciona
Para **impedir rollback por versão monotônica**, clientes verificam Root, Timestamp, Snapshot e Targets segundo limiares, hashes, versões e expirações definidos. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Armazene estado de versão do cliente de teste e sirva uma cópia antiga de metadata. Teste em staging autorizado.

## Limites e trade-offs
Cliente sem persistência confiável de estado pode perder proteção entre reinstalações. Exceções exigem responsável e prazo.

## Como verificar
Confirme rejeição do snapshot com versão menor que a versão previamente aceita. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[tuf-detectar-freeze-com-expiracao]] — Complementa o tópico com the update framework (tuf): detectar freeze com expiração.

## Fontes
- [TUF — Metadata](https://theupdateframework.io/docs/metadata/) — documentação oficial de papéis, metadados, assinaturas, hashes e expiração; consultado em 2026-10-04.
- [TUF — Specification](https://github.com/theupdateframework/specification/blob/master/tuf-spec.md) — especificação oficial de protocolo e verificação de atualizações; consultado em 2026-10-04.
