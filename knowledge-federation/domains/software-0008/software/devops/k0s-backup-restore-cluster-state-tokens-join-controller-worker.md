---
id: software.devops.tranche17.001690
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-17.md"
fontes: ["https://raw.githubusercontent.com/k0sproject/k0s/main/README.md", "https://docs.k0sproject.io/stable/architecture/", "https://github.com/k0sproject/k0s"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# k0s: geração de tokens de ingresso (`k0s token create`) com expiração por papel e backup/restore nativo (`k0s backup`)

## Em uma frase
O `k0s` separa estritamente os tokens de bootstrap por função (`--role=worker` vs `--role=controller` com `--expiry`) e provê os subcomandos nativos `k0s backup` e `k0s restore` para salvar e restaurar um arquivo `.tar.gz` completo com o estado do datastore, certificados PKI e manifestos de deploy.

## Por que importa
Se o mesmo token de join usado para adicionar centenas de worker nodes de borda também tivesse permissão para ingressar um novo nó controlador no quórum `etcd`, o comprometimento físico de um único worker de borda permitiria assumir o controle total do plano de controle.

## Como funciona
O token gerado por `k0s token create --role=worker --expiry=24h` contém apenas credenciais de bootstrap de `kubelet` restritas a nós workers, enquanto `--role=controller` autoriza chamadas na porta `9443` da API de join do controlador. Para proteção de desastres, `sudo k0s backup --save-path /backups/` gera um tarball datado contendo o snapshot do `etcd`/SQLite e toda a PKI de `/var/lib/k0s/pki`.

## Exemplo
```bash
sudo k0s token create --role=worker --expiry=4h > worker.token
sudo k0s backup --save-path /tmp/
ls -lh /tmp/k0s_backup_*.tar.gz
```

## Limites e trade-offs
O comando `k0s restore <arquivo-backup.tar.gz>` deve ser executado em um nó controlador onde o serviço `k0s` ainda não foi iniciado (antes de `k0s start`), restaurando o estado antes da subida do `etcd` e do `kube-apiserver`.

## Como verificar
Gere um backup de teste com `sudo k0s backup --save-path /tmp/` e liste o conteúdo do arquivo `.tar.gz` gerado com `tar -ztvf /tmp/k0s_backup_*.tar.gz`.

## Conexões
- [[k0s-cri-runtimes-containerd-padrao-custom-cri-gvisor-kata]] — Veja também: k0s: gerenciamento do `containerd` embutido, importação de bundles airgap e configuração de CRI customizado.

## Fontes
- [k0s GitHub — README.md (Zero-Friction Kubernetes in a Single Binary, Konnectivity, Kube-Router, kine, k0sctl & Multi-Arch RISC-V/ARM/x86)](https://raw.githubusercontent.com/k0sproject/k0s/main/README.md) — README oficial do k0sproject/k0s (CNCF Sandbox) detalhando empacotamento em binário único, isolamento do control plane, opções de storage/CNI e suporte multi-arquitetura; consultado em 2026-10-03.
- [k0s Official Documentation — Architecture (Process Supervisor, Naked Control Plane Processes, In-Cluster Autopilot & CRI/Worker Runtime)](https://docs.k0sproject.io/stable/architecture/) — Documentação oficial de arquitetura do k0s detalhando supervisão de processos sem container engine no controller, gerenciamento de etcd/kine e containerd nos workers; consultado em 2026-10-03.
- [k0s — Official GitHub Repository](https://github.com/k0sproject/k0s) — Repositório oficial Apache-2.0 do k0s na CNCF; consultado em 2026-10-03.
