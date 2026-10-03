---
id: software.devops.tranche06.000542
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

# Os seis mecanismos de transporte de imagem e armazenamento suportados pelo Skopeo

## Em uma frase
O README oficial documenta os **seis prefixos de transporte** sobre os quais o Skopeo opera para ler, copiar, inspecionar ou sincronizar imagens: (1) **`containers-storage:docker-reference`** — imagem localizada no store local `containers/storage` definido em `/etc/containers/storage.conf` (o backend compartilhado por **Podman, CRI-O e Buildah**); (2) **`dir:path`** — diretório local existente que armazena o manifesto, tarballs de camadas e assinaturas como arquivos individuais (formato não padronizado, útil para depuração e inspeção não invasiva); (3) **`docker://docker-reference`** — imagem em um registro que implementa a *Docker Registry HTTP API V2* (como `docker.io`, `quay.io` ou registros privados); (4) **`docker-archive:path[:docker-reference]`** — arquivo no formato gerado por `docker save` (onde a referência não deve conter digest na criação); (5) **`docker-daemon:docker-reference`** — imagem armazenada no daemon interno do Docker; e (6) **`oci:path:tag`** — imagem em diretório compatível com a *Open Container Image Layout Specification*.

## Por que importa
Dominar esses seis transportes permite converter e mover imagens entre qualquer formato: de um registro remoto `docker://` para um diretório `oci:` ou `dir:` para inspeção forense de camadas, ou do store do Buildah/Podman (`containers-storage:`) diretamente para um tarball `docker-archive:` sem passar por um daemon Docker.

## Como funciona
Especifique sempre o prefixo de transporte explícito na origem e no destino dos comandos do Skopeo (`docker://`, `oci:`, `dir:`, `containers-storage:`, `docker-archive:`, `docker-daemon:`).

## Exemplo
Para inspecionar o conteúdo exato dos arquivos de cada camada de uma imagem suspeita sem executá-la, um analista de segurança executa `skopeo copy docker://exemplo/app:latest dir:/tmp/inspecao-app` e analisa os tarballs extraídos em `/tmp/inspecao-app`.

## Limites e trade-offs
Observe a regra documentada no README para o transporte `docker-archive:path[:docker-reference]`: ao criar um arquivo nesse formato, a `docker-reference` opcional **não deve conter um digest**, enquanto em `docker-daemon:docker-reference` a referência deve conter uma tag ou um digest (ou `docker-daemon:algo:digest` ao ler).

## Como verificar
Converta uma imagem pequena de teste para o layout OCI local com `skopeo copy docker://<imagem> oci:/tmp/teste-oci:latest` e verifique o diretório criado.

## Conexões
- [[skopeo-remote-image-inspection-without-pulling-layers]] — Veja também: Inspeção remota de manifestos, tags, camadas e configuração com skopeo inspect sem baixar a imagem.
- [[skopeo-registry-to-registry-copy-without-local-daemon]] — Veja também: Promoção e cópia direta de imagens entre registros com skopeo copy sem daemon local.

## Fontes
- [Skopeo GitHub — README.md (Daemonless & Rootless Image Operations, 6 Storage Transports, Inspect, Copy, Sync & Auth)](https://raw.githubusercontent.com/containers/skopeo/main/README.md) — README oficial do Skopeo (Apache-2.0) detalhando operações em imagens OCI e Docker v2 sem exigir root nem daemon, os 6 tipos de transporte (containers-storage:, dir:, docker://, docker-archive:, docker-daemon:, oci:), inspeção remota sem pull (skopeo inspect e --config), cópia entre registros/transportes (skopeo copy), sincronização air-gapped (skopeo sync), autenticação ($XDG_RUNTIME_DIR/containers/auth.json, --creds, --src-creds, --dest-creds), alerta contra sites falsos não afiliados e tabela dos 11 subcomandos CLI.; consultado em 2026-10-03.
- [Skopeo Official Container Image — containers/image_build/skopeo/README.md](https://github.com/containers/image_build/blob/main/skopeo/README.md) — Documentação oficial da imagem de contêiner upstream do Skopeo publicada em quay.io/skopeo/stable.; consultado em 2026-10-03.
- [Skopeo — Official GitHub Repository](https://github.com/containers/skopeo) — Repositório oficial Apache-2.0 do Skopeo (única fonte upstream oficial junto à imagem quay.io/skopeo/stable).; consultado em 2026-10-03.
