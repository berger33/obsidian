---
id: software.devops.tranche09.000885
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

# Telepresence: importação de variáveis de ambiente (--env-file) e montagem de volumes remotos (--mount) no processo local

## Em uma frase
Durante uma anexação (`intercept`, `replace`, `wiretap` ou `ingest`), o Telepresence captura todas as variáveis de ambiente (ConfigMaps e Secrets) e monta os volumes do container remoto (incluindo tokens de ServiceAccount e certificados) para que o processo local se comporte exatamente como dentro do cluster.

## Por que importa
Mesmo que o tráfego de rede chegue ao processo local, a aplicação falhará na partida se não tiver acesso às dezenas de variáveis de ambiente injetadas por `ConfigMap`/`Secret` no Kubernetes ou aos arquivos montados em `/var/run/secrets/kubernetes.io/serviceaccount` e volumes CSI. O README oficial do Telepresence destaca `Remote environment, local process` como funcionalidade essencial.

## Como funciona
Quando o desenvolvedor inicia uma sessão de anexação: (1) **Variáveis de ambiente**: o `Traffic Agent` extrai o ambiente do container remoto; o desenvolvedor pode gravá-lo em um arquivo `.env` local com `--env-file .env.telepresence` (ou `--env-json`) para carregar no debugger do VS Code / GoLand / IntelliJ, ou passar `-- <comando>` na própria linha do `telepresence intercept` para que o Telepresence já injete todas as variáveis diretamente no subprocesso local; e (2) **Volumes remotos (`--mount`)**: o `Traffic Agent` exporta os pontos de montagem de volumes do container remoto (via SFTP/FUSE ou SMB) e o Telepresence os monta em um diretório local (expondo o caminho raiz montado na variável **`$TELEPRESENCE_ROOT`**).

## Exemplo
```bash
# Interceptar um serviço exportando as variáveis remotas do pod para um arquivo .env e executando o binário local já com o ambiente injetado
telepresence intercept payment-worker \
  --port 8080 \
  --env-file ./payment-remote.env \
  -- go run ./cmd/worker
```

## Limites e trade-offs
Como os sistemas de arquivos do Linux/macOS na máquina do desenvolvedor não permitem que um processo sem root sobrescreva diretórios raiz do sistema como `/var/run/secrets` ou `/etc/config`, os volumes do container são montados sob o diretório prefixado **`$TELEPRESENCE_ROOT`** (por exemplo, `$TELEPRESENCE_ROOT/var/run/secrets/...`), a menos que se utilize execução em container Docker local (`--docker-run`) onde os volumes são montados nos caminhos absolutos exatos.

## Como verificar
Dentro de um processo iniciado pelo `telepresence intercept ... -- env`, verifique que as variáveis vindas dos ConfigMaps e Secrets do pod remoto e a variável `TELEPRESENCE_ROOT` estão presentes.

## Conexões
- [[telepresence-modos-traffic-agent-sidecar-vs-node-agent]] — Veja também: Telepresence: escolha entre Traffic Agent como Sidecar injetado (padrão) ou Node-Agent sem reiniciar pods.
- [[telepresence-rede-virtual-vif-dns-cluster-sem-port-forward]] — Veja também: Telepresence: dispositivo de rede virtual (VIF) no Root-Daemon, resolução DNS do cluster e roteamento direto de IPs.
- [[telepresence-desenvolvimento-local-remoto-kubernetes-arquitetura]] — Referência cruzada direta com telepresence-desenvolvimento-local-remoto-kubernetes-arquitetura.
- [[telepresence-quatro-modos-anexacao-replace-intercept-wiretap-ingest]] — Referência cruzada direta com telepresence-quatro-modos-anexacao-replace-intercept-wiretap-ingest.
- [[telepresence-execucao-containers-docker-run-docker-build]] — Referência cruzada direta com telepresence-execucao-containers-docker-run-docker-build.

## Fontes
- [Telepresence GitHub — README.md (CNCF Local-to-Cluster Development, 4 Attachment Modes & Traffic Filtering)](https://raw.githubusercontent.com/telepresenceio/telepresence/release/v2/README.md) — README oficial do Telepresence (v2) detalhando eliminação do ciclo build/push/deploy, modos replace/intercept/wiretap/ingest, filtragem HTTP para equipes e importação de ambiente/volumes; consultado em 2026-10-03.
- [Telepresence Official Documentation — Architecture (User-Daemon, Root-Daemon VIF, Traffic Manager & Sidecar vs Node-Agent)](https://telepresence.io/docs/concepts/architecture) — Documentação oficial de arquitetura do Telepresence v2.32 explicando User-Daemon, Root-Daemon (Virtual Network Device VIF), Traffic Manager (telepresence helm install) e Traffic Agent como sidecar ou node-agent sem restart; consultado em 2026-10-03.
- [Telepresence — Official GitHub Repository](https://github.com/telepresenceio/telepresence) — Repositório oficial Apache-2.0 do Telepresence na CNCF; consultado em 2026-10-03.
