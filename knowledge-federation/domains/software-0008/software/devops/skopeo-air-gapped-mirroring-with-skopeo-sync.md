---
id: software.devops.tranche06.000544
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

# Sincronização de repositórios para ambientes desconectados (air-gapped) com skopeo sync

## Em uma frase
Para ambientes desconectados da internet (**air-gapped deployments**) ou espelhamento em lote de repositórios inteiros, o README oficial destaca o subcomando **`skopeo-sync(1)`** (`skopeo sync`). Em vez de copiar apenas uma tag individual por vez como no `skopeo copy`, o `skopeo sync` sincroniza múltiplas tags de um repositório de origem para um diretório local/mídia removível ou diretamente para um registro interno — como no exemplo oficial **`skopeo sync --src docker --dest dir registry.example.com/busybox /media/usb`**.

## Por que importa
Em data centers industriais, militares, financeiros ou de borda que operam totalmente isolados da internet (air-gapped), transportar dezenas de versões de imagens de operadores Kubernetes (como Strimzi, Rook, MetalLB e CRI-O) tag por tag manualmente é inviável e propenso a esquecimentos. O `skopeo sync` automatiza tanto a exportação para disco (`--src docker --dest dir`) quanto a importação posterior do disco para o registro interno (`--src dir --dest docker`).

## Como funciona
Utilize `skopeo sync` (com argumentos de linha de comando ou arquivo YAML de configuração de imagens filtradas) para espelhar repositórios externos homologados para um diretório intermediário e, na rede interna, sincronizar desse diretório para o registro privado corporativo.

## Exemplo
Antes de uma atualização trimestral de um cluster Kubernetes air-gapped, a equipe executa `skopeo sync --src docker --dest dir` em uma máquina conectada para salvar todas as imagens da release em um volume externo assinado e, dentro do data center isolado, executa `skopeo sync --src dir --dest docker` para popular o registro interno.

## Limites e trade-offs
Valide o espaço em disco disponível no destino antes de rodar `skopeo sync` sem filtro de tags contra um repositório público antigo, pois um repositório sem filtro pode conter centenas de tags históricas acumuladas ao longo de anos.

## Como verificar
Teste `skopeo sync --src oci --dest dir` em um repositório OCI local de teste e verifique a estrutura de diretórios sincronizada.

## Conexões
- [[skopeo-registry-to-registry-copy-without-local-daemon]] — Veja também: Promoção e cópia direta de imagens entre registros com skopeo copy sem daemon local.
- [[skopeo-authentication-flows-login-auth-json-and-creds-flags]] — Veja também: Gerenciamento de autenticação em registros com skopeo login, auth.json e flags --creds, --src-creds e --dest-creds.

## Fontes
- [Skopeo GitHub — README.md (Daemonless & Rootless Image Operations, 6 Storage Transports, Inspect, Copy, Sync & Auth)](https://raw.githubusercontent.com/containers/skopeo/main/README.md) — README oficial do Skopeo (Apache-2.0) detalhando operações em imagens OCI e Docker v2 sem exigir root nem daemon, os 6 tipos de transporte (containers-storage:, dir:, docker://, docker-archive:, docker-daemon:, oci:), inspeção remota sem pull (skopeo inspect e --config), cópia entre registros/transportes (skopeo copy), sincronização air-gapped (skopeo sync), autenticação ($XDG_RUNTIME_DIR/containers/auth.json, --creds, --src-creds, --dest-creds), alerta contra sites falsos não afiliados e tabela dos 11 subcomandos CLI.; consultado em 2026-10-03.
- [Skopeo Official Container Image — containers/image_build/skopeo/README.md](https://github.com/containers/image_build/blob/main/skopeo/README.md) — Documentação oficial da imagem de contêiner upstream do Skopeo publicada em quay.io/skopeo/stable.; consultado em 2026-10-03.
- [Skopeo — Official GitHub Repository](https://github.com/containers/skopeo) — Repositório oficial Apache-2.0 do Skopeo (única fonte upstream oficial junto à imagem quay.io/skopeo/stable).; consultado em 2026-10-03.
