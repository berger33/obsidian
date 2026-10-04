---
id: software.seguranca.tranche20.001920
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

# The Update Framework (TUF): Bootstrap seguro do primeiro Root

## Em uma frase
**The Update Framework (TUF) — Bootstrap seguro do primeiro Root:** Clientes precisam obter uma root inicial por canal confiável antes de verificar o restante do repositório.

## Por que importa
O recorte de **bootstrap seguro do primeiro root** ajuda a proteger clientes de atualização com papéis de metadados separados, hashes, versões e limites de assinatura. A equipe registra risco, evidência e responsável.

## Como funciona
Para **bootstrap seguro do primeiro root**, clientes verificam Root, Timestamp, Snapshot e Targets segundo limiares, hashes, versões e expirações definidos. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Distribua root inicial pelo pacote assinado do cliente em ambiente de teste. Teste em staging autorizado.

## Limites e trade-offs
Se root inicial vier do mesmo canal não autenticado do payload, bootstrap perde sentido. Exceções exigem responsável e prazo.

## Como verificar
Documente fingerprint, canal de distribuição e procedimento de atualização inicial. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[openvex-modelar-statement-de-vulnerabilidade]] — Complementa o tópico com openvex: modelar statement de vulnerabilidade.

## Fontes
- [TUF — Metadata](https://theupdateframework.io/docs/metadata/) — documentação oficial de papéis, metadados, assinaturas, hashes e expiração; consultado em 2026-10-04.
- [TUF — Specification](https://github.com/theupdateframework/specification/blob/master/tuf-spec.md) — especificação oficial de protocolo e verificação de atualizações; consultado em 2026-10-04.
