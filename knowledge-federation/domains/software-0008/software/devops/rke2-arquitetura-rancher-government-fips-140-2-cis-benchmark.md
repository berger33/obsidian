---
id: software.devops.tranche17.001671
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
fontes: ["https://raw.githubusercontent.com/rancher/rke2/master/README.md", "https://docs.rke2.io/architecture", "https://github.com/rancher/rke2"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# RKE2 (RKE Government): arquitetura da distribuição Kubernetes da Rancher com conformidade FIPS 140-2 e CIS Benchmark

## Em uma frase
O RKE2 (também conhecido como *RKE Government*) é a distribuição Kubernetes de próxima geração da Rancher (SUSE), totalmente conformante com a CNCF, que combina a simplicidade operacional de binário único do K3s com os componentes upstream do Kubernetes compilados estaticamente com `Go+BoringCrypto` para conformidade **FIPS 140-2** e **CIS Kubernetes Benchmark**.

## Por que importa
Enquanto o K3s substitui componentes ou embute o control plane em um único processo para minimizar memória na borda, setores governamentais, financeiros e corporativos exigem componentes upstream isolados em Static Pods, suporte a SELinux/MCS e criptografia validada por FIPS.

## Como funciona
O binário `rke2` atua como supervisor de bootstrap: ele extrai da imagem `rancher/rke2-runtime` os binários de operação (`containerd`, `runc`, `kubelet`, `kubectl`, `crictl`, `ctr`, `socat`) para `/var/lib/rancher/rke2/data/${RKE2_DATA_KEY}/bin`, inicia o `containerd` e o `kubelet`, e nos nós `server` provisiona `etcd`, `kube-apiserver`, `kube-controller-manager` e `kube-scheduler` como Static Pods em `/var/lib/rancher/rke2/agent/pod-manifests/`, além do `helm-controller` embutido.

## Exemplo
```bash
curl -sfL https://get.rke2.io | sh -
systemctl enable rke2-server.service
systemctl start rke2-server.service
export KUBECONFIG=/etc/rancher/rke2/rke2.yaml PATH=$PATH:/var/lib/rancher/rke2/bin
kubectl get nodes
```

## Limites e trade-offs
Todos os componentes core compilados em Go no RKE2 (exceto o Traefik) são ligados estaticamente com `Go+BoringCrypto`, e a pipeline de build escaneia regularmente todas as imagens com Trivy antes de cada release.

## Como verificar
Execute `kubectl get pods -n kube-system` usando o `rke2.yaml` gerado e confirme a execução dos Static Pods do control plane e do CNI.

## Conexões
- [[rke2-content-bootstrap-rke2-runtime-data-key-airgap-tarballs]] — Veja também: RKE2: processo de *Content Bootstrap* a partir da imagem `rancher/rke2-runtime` e tarballs air-gapped.

## Fontes
- [RKE2 GitHub — README.md (Rancher's Next-Gen Kubernetes Distribution / RKE Government, FIPS 140-2, CIS Hardening & Configuration File)](https://raw.githubusercontent.com/rancher/rke2/master/README.md) — README oficial do rancher/rke2 detalhando conformidade FIPS 140-2 com Go+BoringCrypto, CIS Benchmark, instalação systemd e /etc/rancher/rke2/config.yaml; consultado em 2026-10-03.
- [RKE2 Official Documentation — Architecture (Content Bootstrap from rke2-runtime, Server/Agent Static Pod Lifecycle, CNI, Traefik & CIS/SELinux)](https://docs.rke2.io/architecture) — Documentação oficial de arquitetura do RKE2 explicando Content Bootstrap, Static Pods do control plane, helm-controller, plugins CNI e transição para Traefik v1.36+; consultado em 2026-10-03.
- [RKE2 — Official GitHub Repository](https://github.com/rancher/rke2) — Repositório oficial Apache-2.0 do Rancher RKE2; consultado em 2026-10-03.
