---
id: software.devops.tranche04.000330
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/sigstore/cosign/main/README.md", "https://docs.sigstore.dev/cosign/signing/overview/", "https://github.com/sigstore/cosign"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Estabilidade da série Cosign 2.x e evolução arquitetural sobre sigstore-go

## Em uma frase
A seção de contribuição do repositório oficial esclarece o roteiro arquitetural do projeto: o **Cosign 2.x** é uma release estável que continua recebendo atualizações periódicas de funcionalidades e correções de bugs sem mudanças que quebrem a compatibilidade da API, enquanto o desenvolvimento da próxima versão principal (next major release) concentra-se na biblioteca unificada **`sigstore-go`** (`github.com/sigstore/sigstore-go`), especialmente em torno de fluxos de bring-your-own keys e assinatura.

## Por que importa
Equipes que integram o Cosign como biblioteca Go ou como ferramenta de linha de comando em plataformas corporativas precisam saber que a API da série 2.x possui compromisso de estabilidade sem breaking changes, enquanto novas integrações programáticas em Go devem acompanhar `sigstore-go`.

## Como funciona
Para automações de CLI e pipelines em produção, padronize na série estável Cosign 2.x mantendo patches em dia; para novas bibliotecas e serviços em Go que implementem verificação ou assinatura Sigstore nativamente, avalie o SDK oficial `sigstore-go`.

## Exemplo
Ao projetar um microserviço interno em Go para validar bundles Sigstore de artefatos corporativos, a equipe de segurança adota `github.com/sigstore/sigstore-go` conforme recomendado pelos mantenedores do Cosign, mantendo o CLI `cosign` v2.x nos jobs de CI.

## Limites e trade-offs
Evite acoplar código Go novo a pacotes internos privados do repositório `sigstore/cosign` que serão substituídos pela arquitetura baseada em `sigstore-go` na próxima versão principal.

## Como verificar
Verifique as dependências Go (`go.mod`) e a versão do CLI nos ambientes de build, garantindo conformidade com Go 1.22+ no desenvolvimento e uso das releases estáveis 2.x em produção.

## Conexões
- [[cosign-troubleshooting-rfc3161-timestamps-and-rekor-v2]] — Veja também: Diagnóstico de falhas de verificação no Cosign: RFC3161 timestamps, Rekor v2 e resiliência de serviços.

## Fontes
- [Sigstore Cosign GitHub — README.md (Keyless Signing, Verification, Air-Gapped, Blobs, Attestations)](https://raw.githubusercontent.com/sigstore/cosign/main/README.md) — README oficial do Sigstore Cosign cobrindo assinatura keyless via OIDC, Fulcio e Rekor, assinatura por chave/KMS, verificação online e air-gapped com TUF trusted_root.json, sign-blob/verify-blob e suporte a artefatos OCI (Tekton, WASM, eBPF) e atestações in-toto.; consultado em 2026-10-03.
- [Sigstore Documentation — Cosign Signing Overview](https://docs.sigstore.dev/cosign/signing/overview/) — Documentação oficial do Sigstore sobre fluxos de assinatura e verificação de contêineres e artefatos com Cosign.; consultado em 2026-10-03.
- [Sigstore Cosign — Official GitHub Repository](https://github.com/sigstore/cosign) — Repositório oficial do Cosign no projeto Sigstore com evolução futura convergente para sigstore-go.; consultado em 2026-10-03.
