---
id: software.devops.tranche16.001531
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

# Carvel imgpkg: empacotamento de configurações e referências de imagens em OCI Bundles imutáveis

## Em uma frase
O Carvel `imgpkg` ("image package", CNCF Carvel) empacota conjuntos de arquivos arbitrários (manifestos Kubernetes, templates `ytt`, charts Helm) juntamente com as referências exatas de todas as imagens OCI das quais eles dependem em um único artefato chamado *Bundle* armazenado em qualquer container registry.

## Por que importa
Quando a configuração YAML de uma aplicação é distribuída em um repositório Git ou arquivo `.tgz` separado das imagens de container no registry, esses dois artefatos facilmente saem de sincronia e exigem mecanismos distintos de autenticação, versionamento e transporte para ambientes isolados (*air-gapped*).

## Como funciona
Um Bundle do `imgpkg` é uma imagem OCI padrão marcada com o label `dev.carvel.imgpkg.bundle` que contém os arquivos de configuração da aplicação e um diretório obrigatório `.imgpkg/` na raiz (com `.imgpkg/images.yml` do tipo `ImagesLock` e opcionalmente `.imgpkg/bundle.yml` do tipo `Bundle`). O `imgpkg` normaliza permissões e timestamps dos arquivos para garantir builds determinísticos (mesmo digest SHA-256 se nada mudou).

## Exemplo
```bash
mkdir -p .imgpkg
kbld -f config/ --imgpkg-lock-output .imgpkg/images.yml
imgpkg push -b ghcr.io/org/payments-bundle:1.0.0 -f config/ -f .imgpkg/
imgpkg pull -b ghcr.io/org/payments-bundle:1.0.0 -o /tmp/payments-bundle
```

## Limites e trade-offs
Ao usar `imgpkg pull -b ...` (em vez de `-i` para imagens comuns), o `imgpkg` valida que o artefato no registry é de fato um Bundle contendo `.imgpkg/images.yml` e reescreve automaticamente as entradas do `ImagesLock` caso o bundle tenha sido copiado para outro registry.

## Como verificar
Execute `imgpkg push` duas vezes seguidas sem alterar os arquivos de entrada e confirme que o digest `@sha256:...` retornado pelo comando é exatamente o mesmo.

## Conexões
- [[carvel-imgpkg-diretorio-metadados-imageslock-bundle-yml]] — Veja também: Carvel imgpkg: estrutura e restrições do diretório `.imgpkg/` (`images.yml` e `bundle.yml`).

## Fontes
- [Carvel imgpkg GitHub — README.md (OCI Bundles, Thick Copy, Air-Gapped Relocation & Deterministic Layers)](https://raw.githubusercontent.com/carvel-dev/imgpkg/develop/README.md) — README oficial do carvel-dev/imgpkg apresentando o conceito de OCI Bundle, comandos push/pull/copy e suporte a ambientes air-gapped; consultado em 2026-10-03.
- [Carvel imgpkg Official Documentation — Resources v0.43.x (Bundle, .imgpkg Directory, ImagesLock, BundleLock, Nested Bundles & ImageLocations)](https://carvel.dev/imgpkg/docs/v0.43.x/resources/) — Referência oficial de recursos do Carvel imgpkg especificando ImagesLock, BundleLock, Nested Bundles recursivos e Locations OCI Image; consultado em 2026-10-03.
- [Carvel imgpkg — Official GitHub Repository](https://github.com/carvel-dev/imgpkg) — Repositório oficial Apache-2.0 do Carvel imgpkg; consultado em 2026-10-03.
