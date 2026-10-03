---
id: software.seguranca.tranche03.000221
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/overview.md", "https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/policies/index.md", "https://github.com/aquasecurity/tracee"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Aqua Security Tracee: arquitetura unificada *"Everything is an Event"* para segurança em runtime e forense com `eBPF`

## Em uma frase
Conforme documentado na visão geral oficial (`docs/docs/overview.md`), o **Tracee** (`aquasecurity/tracee`, mantido pela Aqua Security sob licença Apache 2.0) é uma ferramenta de **segurança em tempo de execução (*Runtime Security*) e investigação forense para Linux e Kubernetes** baseada na tecnologia **eBPF (*Extended Berkeley Packet Filter*, com suporte a CO-RE — *Compile Once, Run Everywhere*)**.

## Por que importa
Em arquiteturas tradicionais, a coleta de chamadas de sistema brutas (observabilidade) e o motor de assinaturas de detecção de ameaças operam como ferramentas separadas; o Tracee unifica ambos sob o princípio arquitetural **"Everything is an Event" (*Tudo é um Evento*)**.

## Como funciona
No Tracee, mais de **400 chamadas de sistema**, eventos de rede (DNS, HTTP, pacotes), eventos de enriquecimento de containers/Kubernetes e **assinaturas de detecção de ameaças de alto nível** (como detecção de execução *fileless* em memória, *rootkits*, roubo de credenciais e escape de container) fluem pelo mesmo pipeline de eventos e podem ser combinados livremente nas mesmas políticas YAML!

## Exemplo
```bash
# Executando o Tracee via container Docker com suporte eBPF CO-RE para monitorar novos containers em tempo real:
docker run --name tracee --rm -it \
  --pid=host --cgroupns=host --privileged \
  -v /etc/os-release:/etc/os-release-host:ro \
  -v /var/run:/var/run:ro \
  aquasec/tracee:latest
```

## Limites e trade-offs
Graças ao **eBPF CO-RE (BTF — *BPF Type Format*)**, o Tracee roda diretamente na grande maioria dos kernels Linux modernos sem precisar instalar *kernel headers* ou o compilador `clang`/`llvm` nos nós de produção.

## Como verificar
Execute `tracee version` e `tracee list` para visualizar todos os eventos de syscall, rede e assinaturas de segurança embutidos.

## Conexões
- [[tracee-policies-yaml-kubernetes-crd-vs-plain-format-64-policies]] — Veja também: Tracee Políticas de Detecção (`Policies`): intercambiabilidade entre formato `Kubernetes CRD` (`tracee.aquasec.com/v1beta1`) e `Plain YAML`.

## Fontes
- [Aqua Security Tracee Official Documentation — Overview (Everything is an Event Architecture, 400+ Syscalls, Built-in Signatures, Forensic Capture & Security Model)](https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/overview.md) — Visão geral oficial da documentação do Tracee detalhando o pipeline unificado de eventos, assinaturas de detecção embutidas, coleta forense e modelo de ameaças; consultado em 2026-10-03.
- [Aqua Security Tracee Official Documentation — Policies Reference (Kubernetes CRD v1beta1 vs Plain Format, 64 Policies, Scopes & Event Filters)](https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/policies/index.md) — Referência oficial de políticas do Tracee explicando a intercambiabilidade entre o formato CRD Kubernetes e Plain YAML, escopos e filtros; consultado em 2026-10-03.
- [Aqua Security Tracee — Official GitHub Repository](https://github.com/aquasecurity/tracee) — Repositório oficial Apache-2.0 do Aqua Security Tracee; consultado em 2026-10-03.
