---
id: software.devops.tranche06.000545
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

# Gerenciamento de autenticação em registros com skopeo login, auth.json e flags --creds, --src-creds e --dest-creds

## Em uma frase
A seção *Authenticating to a registry* do README oficial documenta a hierarquia de credenciais utilizada pelo Skopeo: ao acessar registros que implementam a API V2 (`docker://`), o Skopeo utiliza por padrão o estado de autorização salvo em **`$XDG_RUNTIME_DIR/containers/auth.json`**, configurado por meio de **`skopeo login --username USER myregistrydomain.com:5000`** (e encerrado com **`skopeo logout`**). Além disso, o Skopeo reconhece automaticamente credenciais gravadas por **`podman login`**, **`buildah login`** ou **`docker login`**, ou permite passar credenciais diretamente por comando via **`--creds=user:password`** (para `skopeo inspect` e `skopeo delete`) e **`--src-creds` / `--dest-creds`** (para `skopeo copy`).

## Por que importa
Compartilhar o mesmo arquivo de autenticação (`$XDG_RUNTIME_DIR/containers/auth.json`) entre `skopeo`, `podman` e `buildah` permite fazer login uma única vez no início do job de CI e executar build (`buildah`), inspeção (`skopeo inspect`) e cópia (`skopeo copy`) de forma integrada.

## Como funciona
Em pipelines de CI/CD, prefira autenticar com `skopeo login --username "$USER" --password-stdin <registry>` (lendo o token via `STDIN` a partir de um segredo seguro e rodando `skopeo logout` ao final) em vez de passar senhas em texto claro na linha de comando via `--creds`, pois argumentos de linha de comando podem aparecer na listagem de processos (`ps`) do host.

## Exemplo
Um estágio de pipeline faz `echo "$REGISTRY_TOKEN" | skopeo login -u "$REGISTRY_USER" --password-stdin registry.corp.internal`, executa `skopeo copy` das imagens homologadas e encerra com `skopeo logout registry.corp.internal`.

## Limites e trade-offs
Lembre-se de que `$XDG_RUNTIME_DIR` é um diretório em memória (`tmpfs`, tipicamente `/run/user/$UID`) que é limpo quando a sessão do usuário termina; em ambientes sem `$XDG_RUNTIME_DIR` definido (como certos containers de CI mínimos), você também pode especificar `--authfile /caminho/auth.json` explicitamente.

## Como verificar
Execute `skopeo login` e `skopeo logout` contra um registro de teste (ou verifique `--authfile`) confirmando a criação e remoção limpa da entrada no arquivo JSON de autenticação.

## Conexões
- [[skopeo-air-gapped-mirroring-with-skopeo-sync]] — Veja também: Sincronização de repositórios para ambientes desconectados (air-gapped) com skopeo sync.
- [[skopeo-deleting-images-and-registry-garbage-collection]] — Veja também: Marcação de imagens para exclusão em registros com skopeo delete e coleta de lixo.

## Fontes
- [Skopeo GitHub — README.md (Daemonless & Rootless Image Operations, 6 Storage Transports, Inspect, Copy, Sync & Auth)](https://raw.githubusercontent.com/containers/skopeo/main/README.md) — README oficial do Skopeo (Apache-2.0) detalhando operações em imagens OCI e Docker v2 sem exigir root nem daemon, os 6 tipos de transporte (containers-storage:, dir:, docker://, docker-archive:, docker-daemon:, oci:), inspeção remota sem pull (skopeo inspect e --config), cópia entre registros/transportes (skopeo copy), sincronização air-gapped (skopeo sync), autenticação ($XDG_RUNTIME_DIR/containers/auth.json, --creds, --src-creds, --dest-creds), alerta contra sites falsos não afiliados e tabela dos 11 subcomandos CLI.; consultado em 2026-10-03.
- [Skopeo Official Container Image — containers/image_build/skopeo/README.md](https://github.com/containers/image_build/blob/main/skopeo/README.md) — Documentação oficial da imagem de contêiner upstream do Skopeo publicada em quay.io/skopeo/stable.; consultado em 2026-10-03.
- [Skopeo — Official GitHub Repository](https://github.com/containers/skopeo) — Repositório oficial Apache-2.0 do Skopeo (única fonte upstream oficial junto à imagem quay.io/skopeo/stable).; consultado em 2026-10-03.
