---
id: software.devops.tranche02.000110
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/crossplane/crossplane/main/README.md", "https://github.com/crossplane/crossplane"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Registro público de adotantes em ADOPTERS.md e conformidade OpenSSF

## Em uma frase
As seções finais e os badges do README destacam o arquivo `ADOPTERS.md` com a lista de usuários publicamente conhecidos do Crossplane, o selo OpenSSF Best Practices (`bestpractices.dev/projects/3260`), a verificação de licenças no FOSSA e a licença Apache 2.0.

## Por que importa
Avaliar a maturidade de governança, a conformidade OpenSSF e os casos reais documentados em `ADOPTERS.md` ajuda arquitetos a sustentar a adoção do Crossplane perante comitês de arquitetura e segurança corporativa.

## Como funciona
Consulte o arquivo `ADOPTERS.md` no repositório oficial para referências de uso em produção e registre sua organização caso queira compartilhar seu caso de uso com a comunidade.

## Exemplo
Durante uma revisão de fornecedores open source, a equipe de segurança valida a licença Apache 2.0 e o badge OpenSSF Best Practices do Crossplane.

## Limites e trade-offs
A presença em `ADOPTERS.md` comprova adoção comunitária, mas cada organização deve executar seus próprios testes de carga, backup de CRDs e recuperação de desastres no cluster de controle.

## Como verificar
Conferi os badges de topo e as seções Adopters e License no README oficial de `crossplane/crossplane`.

## Conexões
- [[crossplane-sig-composition-and-provider-ecosystems]] — Veja também: Frentes técnicas dos 14 SIGs: composição, provedores, Upjet e observabilidade.

## Fontes
- [Crossplane — GitHub README](https://raw.githubusercontent.com/crossplane/crossplane/main/README.md) — Visão geral do Crossplane como framework de control planes cloud-native na CNCF, tabela de releases e EOL (v1.20 e v2.2–v2.7), roadmap, reuniões e 14 SIGs.; consultado em 2026-10-03.
- [Crossplane — Repositório Oficial no GitHub](https://github.com/crossplane/crossplane) — Repositório oficial do Crossplane com código-fonte, ADOPTERS.md, contributing/README.md e notas de release.; consultado em 2026-10-03.
