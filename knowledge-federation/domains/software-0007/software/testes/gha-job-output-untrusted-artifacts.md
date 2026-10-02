---
id: software.testes.tranche08.000228
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-08.md"
fontes: ["https://docs.github.com/en/actions/reference/security/secure-use", "https://docs.github.com/en/actions/tutorials/store-and-share-data"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GitHub Actions: não confiar em artifacts de execução não privilegiada

## Em uma frase
Valide origem e conteúdo de artifacts antes de consumi-los em job com permissões maiores.

## Por que importa
Código não confiável pode publicar artefato manipulado que um workflow privilegiado executa ou interpreta como dado confiável.

## Como funciona
Separe construção e publicação, associe artifact ao run e commit esperados, verifique conteúdo e nunca execute scripts baixados sem validação.

## Exemplo
Um job de deploy baixa pacote de build de workflow protegido, confere checksum e metadado; não usa artifact vindo de fork como comando.

## Limites e trade-offs
Checksum fornecido pelo mesmo produtor comprometido não atesta origem; cadeia de confiança e identidade do workflow também importam.

## Como verificar
Tente fornecer artifact de run diferente e confirme rejeição; examine steps que extraem, executam ou interpolam seu conteúdo.

## Conexões
- [[gha-artifact-retention-provenance]] — Veja também: GitHub Actions: reter artifacts sem perder proveniência.
- [[gha-pinning-third-party-actions]] — Veja também: GitHub Actions: fixar e revisar actions de terceiros.

## Fontes
- [GitHub Actions — Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) — least privilege, secrets, script injection e revisão de logs; consultado em 2026-10-02.
- [GitHub Actions — Store and share data](https://docs.github.com/en/actions/tutorials/store-and-share-data) — upload, download e retenção de artifacts; consultado em 2026-10-02.
