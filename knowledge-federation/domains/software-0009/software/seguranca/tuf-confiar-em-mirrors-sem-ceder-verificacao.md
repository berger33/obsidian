---
id: software.seguranca.tranche20.001919
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

# The Update Framework (TUF): Confiar em mirrors sem ceder verificação

## Em uma frase
**The Update Framework (TUF) — Confiar em mirrors sem ceder verificação:** Mirrors podem servir metadados e payloads, enquanto cliente valida assinaturas e hashes independentemente.

## Por que importa
O recorte de **confiar em mirrors sem ceder verificação** ajuda a proteger clientes de atualização com papéis de metadados separados, hashes, versões e limites de assinatura. A equipe registra risco, evidência e responsável.

## Como funciona
Para **confiar em mirrors sem ceder verificação**, clientes verificam Root, Timestamp, Snapshot e Targets segundo limiares, hashes, versões e expirações definidos. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Configure mirror de teste com bytes alterados e use client TUF para verificar integridade. Teste em staging autorizado.

## Limites e trade-offs
Mirror confiável para disponibilidade não deve ser tratado como raiz de autoridade. Exceções exigem responsável e prazo.

## Como verificar
Demonstre que cliente aceita mirror correto e recusa metadata ou target adulterado. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[tuf-bootstrap-seguro-do-primeiro-root]] — Complementa o tópico com the update framework (tuf): bootstrap seguro do primeiro root.

## Fontes
- [TUF — Metadata](https://theupdateframework.io/docs/metadata/) — documentação oficial de papéis, metadados, assinaturas, hashes e expiração; consultado em 2026-10-04.
- [TUF — Specification](https://github.com/theupdateframework/specification/blob/master/tuf-spec.md) — especificação oficial de protocolo e verificação de atualizações; consultado em 2026-10-04.
