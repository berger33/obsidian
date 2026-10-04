---
id: software.devops.tranche09.000887
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/telepresenceio/telepresence/release/v2/README.md", "https://telepresence.io/docs/concepts/architecture", "https://github.com/telepresenceio/telepresence"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Telepresence: execução de interceptações em containers Docker locais (--docker-run, --docker-build e telepresence connect --docker)

## Em uma frase
O Telepresence permite executar o processo local dentro de um container Docker (`--docker-run`, `--docker-build`) conectado à rede do cluster (`telepresence connect --docker`), montando volumes remotos em seus caminhos absolutos exatos (`/var/run/secrets/...`) e dispensando privilégios `sudo` no host.

## Por que importa
Em máquinas onde o desenvolvedor não possui permissão de administrador (`sudo`) para criar interfaces `tun` (`VIF`) no sistema operacional hospedeiro, ou quando a aplicação exige bibliotecas específicas do Linux e caminhos absolutos hardcoded (como `/etc/certs/tls.crt` que não podem ser montados na raiz do macOS/Windows), rodar o processo interceptado em um container Docker local resolve ambas as limitações.

## Como funciona
Quando o usuário inicia a conexão com **`telepresence connect --docker`** (ou usa `--docker-run` diretamente no `intercept`), o Telepresence inicia o daemon de rede dentro de um container Docker local na estação de trabalho em vez de modificar a tabela de rotas e o DNS do sistema operacional hospedeiro. Ao executar **`telepresence intercept meu-app --port 8080 --docker-run -- minha-imagem:dev`** (ou `--docker-build ./caminho-do-contexto`), o Telepresence inicia o container da aplicação compartilhando o namespace de rede do container daemon do Telepresence, injeta todas as variáveis de ambiente do pod remoto e monta os volumes remotos exatamente nos mesmos caminhos absolutos do pod Kubernetes.

## Exemplo
```bash
# Interceptar um workload rodando o código local dentro de um container Docker sem alterar o DNS/rotas do host
telepresence intercept billing-api --port 8080:8080 --docker-run -- billing-api:local-dev
```

## Limites e trade-offs
Ao usar `telepresence connect --docker`, apenas processos que rodam dentro de containers conectados àquela rede Docker do Telepresence enxergam o DNS e os IPs internos do cluster Kubernetes; aplicações rodando diretamente no host fora do Docker (como o navegador web ou um cliente GUI) não terão rota direta para `*.svc.cluster.local` a menos que você use o `telepresence connect` padrão no host.

## Como verificar
Execute `docker ps` durante uma sessão com `--docker-run` para verificar o container local em execução conectado à rede do Telepresence e valide o acesso aos caminhos absolutos de volumes montados.

## Conexões
- [[telepresence-rede-virtual-vif-dns-cluster-sem-port-forward]] — Veja também: Telepresence: dispositivo de rede virtual (VIF) no Root-Daemon, resolução DNS do cluster e roteamento direto de IPs.
- [[telepresence-gerenciamento-traffic-manager-helm-namespaces-rbac]] — Veja também: Telepresence: instalação e administração do Traffic Manager no cluster (telepresence helm install/upgrade) e escopo de namespaces.
- [[telepresence-desenvolvimento-local-remoto-kubernetes-arquitetura]] — Referência cruzada direta com telepresence-desenvolvimento-local-remoto-kubernetes-arquitetura.
- [[telepresence-ambiente-remoto-variaveis-montagem-volumes-locais]] — Referência cruzada direta com telepresence-ambiente-remoto-variaveis-montagem-volumes-locais.

## Fontes
- [Telepresence GitHub — README.md (CNCF Local-to-Cluster Development, 4 Attachment Modes & Traffic Filtering)](https://raw.githubusercontent.com/telepresenceio/telepresence/release/v2/README.md) — README oficial do Telepresence (v2) detalhando eliminação do ciclo build/push/deploy, modos replace/intercept/wiretap/ingest, filtragem HTTP para equipes e importação de ambiente/volumes; consultado em 2026-10-03.
- [Telepresence Official Documentation — Architecture (User-Daemon, Root-Daemon VIF, Traffic Manager & Sidecar vs Node-Agent)](https://telepresence.io/docs/concepts/architecture) — Documentação oficial de arquitetura do Telepresence v2.32 explicando User-Daemon, Root-Daemon (Virtual Network Device VIF), Traffic Manager (telepresence helm install) e Traffic Agent como sidecar ou node-agent sem restart; consultado em 2026-10-03.
- [Telepresence — Official GitHub Repository](https://github.com/telepresenceio/telepresence) — Repositório oficial Apache-2.0 do Telepresence na CNCF; consultado em 2026-10-03.
