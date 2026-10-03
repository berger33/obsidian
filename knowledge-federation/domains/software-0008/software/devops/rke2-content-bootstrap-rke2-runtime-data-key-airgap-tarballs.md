---
id: software.devops.tranche17.001672
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
fontes: ["https://docs.rke2.io/architecture", "https://raw.githubusercontent.com/rancher/rke2/master/README.md", "https://github.com/rancher/rke2"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# RKE2: processo de *Content Bootstrap* a partir da imagem `rancher/rke2-runtime` e tarballs air-gapped

## Em uma frase
Durante a inicialização (*Content Bootstrap*), o RKE2 obtém todos os binários de host (`containerd`, `kubelet`, `runc`, `kubectl`, `crictl`, `ctr`, `socat`) e os charts de sistema a partir da imagem OCI `rancher/rke2-runtime` (local em `/var/lib/rancher/rke2/agent/images/*.tar` ou baixada da rede).

## Por que importa
Empacotar binários do sistema operacional e manifestos de bootstrap dentro de uma imagem de container assinada permite atualizar ou instalar o cluster inteiro de forma atômica e reproduzível em ambientes air-gapped apenas copiando arquivos `.tar`.

## Como funciona
Ao iniciar, o `rke2` verifica `/var/lib/rancher/rke2/agent/images/*.tar` buscando a imagem `rancher/rke2-runtime` correspondente à saída de `rke2 --version` (fazendo pull se não encontrar localmente). Em seguida, extrai `/bin/` para `/var/lib/rancher/rke2/data/${RKE2_DATA_KEY}/bin` e extrai os charts Helm base para `/var/lib/rancher/rke2/server/manifests`.

## Exemplo
```bash
ls -la /var/lib/rancher/rke2/data/
ls -la /var/lib/rancher/rke2/server/manifests/
/var/lib/rancher/rke2/bin/crictl ps
```

## Limites e trade-offs
Como os binários operacionais (`kubectl`, `crictl`, `ctr`) ficam dentro de `/var/lib/rancher/rke2/bin` (um symlink para o diretório `${RKE2_DATA_KEY}/bin` ativo), eles não são adicionados automaticamente ao `/usr/local/bin` por padrão para não colidir com pacotes do sistema.

## Como verificar
Adicione `/var/lib/rancher/rke2/bin` ao `PATH` e configure `CRI_CONFIG_FILE=/var/lib/rancher/rke2/agent/etc/crictl.yaml` para inspecionar containers diretamente via `crictl ps`.

## Conexões
- [[rke2-arquitetura-rancher-government-fips-140-2-cis-benchmark]] — Veja também: RKE2 (RKE Government): arquitetura da distribuição Kubernetes da Rancher com conformidade FIPS 140-2 e CIS Benchmark.
- [[rke2-config-yaml-systemd-precedencia-flags-cli-listas]] — Veja também: RKE2: configuração declarativa em `/etc/rancher/rke2/config.yaml` e regras de precedência com flags CLI.

## Fontes
- [RKE2 GitHub — README.md (Rancher's Next-Gen Kubernetes Distribution / RKE Government, FIPS 140-2, CIS Hardening & Configuration File)](https://docs.rke2.io/architecture) — README oficial do rancher/rke2 detalhando conformidade FIPS 140-2 com Go+BoringCrypto, CIS Benchmark, instalação systemd e /etc/rancher/rke2/config.yaml; consultado em 2026-10-03.
- [RKE2 Official Documentation — Architecture (Content Bootstrap from rke2-runtime, Server/Agent Static Pod Lifecycle, CNI, Traefik & CIS/SELinux)](https://raw.githubusercontent.com/rancher/rke2/master/README.md) — Documentação oficial de arquitetura do RKE2 explicando Content Bootstrap, Static Pods do control plane, helm-controller, plugins CNI e transição para Traefik v1.36+; consultado em 2026-10-03.
- [RKE2 — Official GitHub Repository](https://github.com/rancher/rke2) — Repositório oficial Apache-2.0 do Rancher RKE2; consultado em 2026-10-03.
