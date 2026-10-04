---
id: software.devops.tranche06.000541
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/containers/skopeo/main/README.md", "https://github.com/containers/image_build/blob/main/skopeo/README.md", "https://github.com/containers/skopeo"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Inspeção remota de manifestos, tags, camadas e configuração com skopeo inspect sem baixar a imagem

## Em uma frase
O `skopeo` (`github.com/containers/skopeo`), licenciado sob Apache-2.0, é um utilitário de linha de comando que executa diversas operações sobre imagens de contêiner (tanto **OCI** quanto **Docker v2**) e repositórios de imagens **sem exigir um daemon em execução e sem exigir privilégios de root** para a maioria de suas operações. Conforme destaca o README oficial, em contraste com o `docker inspect` tradicional (que exige baixar toda a imagem para o disco local primeiro via `docker pull`), o comando **`skopeo inspect docker://registry.fedoraproject.org/fedora:latest`** busca apenas o manifesto remoto no registro e exibe em JSON o `Digest`, `RepoTags`, `Created`, `Labels`, `Architecture`, `Os`, `Layers`, `LayersData` (com tamanho em bytes e MIMEType de cada camada) e `Env` **sem baixar os gigabytes das camadas para o host**. Passando a flag **`--config`**, `skopeo inspect --config` exibe também o JSON completo de configuração interna da imagem (`cmd`, `rootfs.diff_ids`, `history`).

## Por que importa
Baixar uma imagem de 3 GB apenas para verificar qual é o seu digest SHA-256, para qual arquitetura de CPU (`amd64` vs `arm64`) ela foi compilada, quais variáveis de ambiente define ou qual o tamanho das camadas desperdiça banda de rede, tempo de CI e espaço em disco.

## Como funciona
Utilize `skopeo inspect docker://<imagem>` e `skopeo inspect --config docker://<imagem> | jq` em scripts de CI/CD e auditoria de segurança para validar metadados, tags disponíveis (`skopeo list-tags`) e digests antes de autorizar o deploy no cluster.

## Exemplo
Antes de atualizar a tag de uma imagem de terceiros no manifesto GitOps, o engenheiro executa `skopeo inspect docker://registry.fedoraproject.org/fedora:latest | jq '.Digest'` para obter o digest imutável SHA-256 em menos de um segundo sem fazer pull das camadas.

## Limites e trade-offs
Quando precisar listar apenas as tags disponíveis em um repositório grande sem buscar metadados extras de uma imagem específica, utilize o subcomando dedicado **`skopeo list-tags`** (`skopeo-list-tags(1)`).

## Como verificar
Execute `skopeo inspect` e `skopeo inspect --config` contra uma imagem pública e confirme o retorno imediato do JSON com `Digest`, `Architecture` e `LayersData`.

## Conexões
- [[skopeo-six-container-storage-and-registry-transports]] — Veja também: Os seis mecanismos de transporte de imagem e armazenamento suportados pelo Skopeo.

## Fontes
- [Skopeo GitHub — README.md (Daemonless & Rootless Image Operations, 6 Storage Transports, Inspect, Copy, Sync & Auth)](https://raw.githubusercontent.com/containers/skopeo/main/README.md) — README oficial do Skopeo (Apache-2.0) detalhando operações em imagens OCI e Docker v2 sem exigir root nem daemon, os 6 tipos de transporte (containers-storage:, dir:, docker://, docker-archive:, docker-daemon:, oci:), inspeção remota sem pull (skopeo inspect e --config), cópia entre registros/transportes (skopeo copy), sincronização air-gapped (skopeo sync), autenticação ($XDG_RUNTIME_DIR/containers/auth.json, --creds, --src-creds, --dest-creds), alerta contra sites falsos não afiliados e tabela dos 11 subcomandos CLI.; consultado em 2026-10-03.
- [Skopeo Official Container Image — containers/image_build/skopeo/README.md](https://github.com/containers/image_build/blob/main/skopeo/README.md) — Documentação oficial da imagem de contêiner upstream do Skopeo publicada em quay.io/skopeo/stable.; consultado em 2026-10-03.
- [Skopeo — Official GitHub Repository](https://github.com/containers/skopeo) — Repositório oficial Apache-2.0 do Skopeo (única fonte upstream oficial junto à imagem quay.io/skopeo/stable).; consultado em 2026-10-03.
