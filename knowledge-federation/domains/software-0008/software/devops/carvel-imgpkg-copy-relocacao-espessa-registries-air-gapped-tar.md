---
id: software.devops.tranche16.001533
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/carvel-dev/imgpkg/develop/README.md", "https://carvel.dev/imgpkg/docs/v0.43.x/resources/", "https://github.com/carvel-dev/imgpkg"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Carvel imgpkg: cópia espessa (*thick copy*) de bundles e imagens dependentes entre registries e tarballs air-gapped

## Em uma frase
O comando `imgpkg copy -b <bundle>` realiza uma cópia espessa (*thick copy*), transferindo em uma única operação tanto a imagem OCI do próprio Bundle quanto todas as imagens de containers e bundles aninhados referenciados em seu `.imgpkg/images.yml`.

## Por que importa
Em instalações desconectadas da internet (*air-gapped*) ou ao promover uma release do registry de desenvolvimento para o registry de produção de um cliente, descobrir manualmente todas as imagens de terceiros usadas pelos manifestos e copiá-las uma a uma sem quebrar os digests é lento e propenso a omissões.

## Como funciona
No modo online, `imgpkg copy -b ghcr.io/org/app-bundle:1.0.0 --to-repo registry.interno.local/corp/app` copia todos os blobs para o repositório de destino mantendo os mesmos digests SHA-256. No modo air-gapped em duas etapas, `--to-tar /midia/bundle.tar` exporta o bundle e todas as imagens dependentes para um único arquivo tar, e `imgpkg copy --tar /midia/bundle.tar --to-repo registry.airgap.local/corp/app` importa tudo na rede isolada.

## Exemplo
```bash
imgpkg copy -b ghcr.io/org/payments-bundle:1.0.0 --to-tar /tmp/payments-airgap.tar
imgpkg copy --tar /tmp/payments-airgap.tar --to-repo registry.airgap.internal/payments/bundle
```

## Limites e trade-offs
Ao copiar para `--to-repo`, todas as imagens dependentes são colocalizadas dentro do mesmo repositório de destino (identificadas por seus digests imutáveis), simplificando permissões de RBAC e criação de repositórios no registry privado.

## Como verificar
Após executar `imgpkg copy --to-repo`, faça `imgpkg pull -b registry.airgap.internal/payments/bundle:1.0.0 -o /tmp/pulled` e verifique que todas as referências em `/tmp/pulled/.imgpkg/images.yml` agora apontam para `registry.airgap.internal/payments/bundle@sha256:...`.

## Conexões
- [[carvel-imgpkg-diretorio-metadados-imageslock-bundle-yml]] — Veja também: Carvel imgpkg: estrutura e restrições do diretório `.imgpkg/` (`images.yml` e `bundle.yml`).
- [[carvel-imgpkg-nested-bundles-composicao-recursiva-sem-limites]] — Veja também: Carvel imgpkg: composição recursiva de Nested Bundles e extração estruturada em disco.

## Fontes
- [Carvel imgpkg GitHub — README.md (OCI Bundles, Thick Copy, Air-Gapped Relocation & Deterministic Layers)](https://raw.githubusercontent.com/carvel-dev/imgpkg/develop/README.md) — README oficial do carvel-dev/imgpkg apresentando o conceito de OCI Bundle, comandos push/pull/copy e suporte a ambientes air-gapped; consultado em 2026-10-03.
- [Carvel imgpkg Official Documentation — Resources v0.43.x (Bundle, .imgpkg Directory, ImagesLock, BundleLock, Nested Bundles & ImageLocations)](https://carvel.dev/imgpkg/docs/v0.43.x/resources/) — Referência oficial de recursos do Carvel imgpkg especificando ImagesLock, BundleLock, Nested Bundles recursivos e Locations OCI Image; consultado em 2026-10-03.
- [Carvel imgpkg — Official GitHub Repository](https://github.com/carvel-dev/imgpkg) — Repositório oficial Apache-2.0 do Carvel imgpkg; consultado em 2026-10-03.
