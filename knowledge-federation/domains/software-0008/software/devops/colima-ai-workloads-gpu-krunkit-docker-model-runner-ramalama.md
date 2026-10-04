---
id: software.devops.tranche15.001444
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/abiosoft/colima/main/README.md", "https://raw.githubusercontent.com/abiosoft/colima/main/docs/FAQ.md", "https://github.com/abiosoft/colima"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Colima: aceleração por GPU para modelos de IA (`--vm-type krunkit`) com Docker Model Runner e Ramalama

## Em uma frase
A partir da versão `v0.10.0` em Apple Silicon (macOS 13+), o Colima suporta containers acelerados por GPU para cargas de trabalho de IA usando o tipo de máquina virtual `krunkit` e o subcomando `colima model`.

## Por que importa
Executar inferência de LLMs (como Gemma 3, Llama 3.2 ou Phi-3) dentro de uma VM Linux tradicional apenas em CPU é proibitivamente lento; o `krunkit` expõe aceleração de GPU da Apple para os containers dentro da VM do Colima.

## Como funciona
Após instalar o `krunkit` e iniciar a instância com `colima start --runtime docker --vm-type krunkit`, o usuário executa modelos diretamente com `colima model run <modelo>`. O Colima suporta dois backends de model runner: o **Docker Model Runner** (padrão, compatível com Docker AI Registry e HuggingFace `hf.co/...`) e o **Ramalama** (compatível com HuggingFace e registros `ollama://`).

## Exemplo
```bash
colima start --runtime docker --vm-type krunkit
colima model run gemma3
colima model run ollama://gemma3 --runner ramalama
```

## Limites e trade-offs
A aceleração de GPU via `krunkit` requer obrigatoriamente Macs com Apple Silicon rodando macOS 13 ou superior e o binário `krunkit` previamente instalado no host.

## Como verificar
Execute `colima model --help` e teste a inferência de um modelo leve verificando o uso de GPU na máquina.

## Conexões
- [[colima-kubernetes-integrado-compartilhamento-imagens-k8s-io]] — Veja também: Colima: cluster Kubernetes local (`--kubernetes`) e compartilhamento direto de imagens com Docker e containerd.
- [[colima-dimensionamento-cpu-memory-disk-vz-rosetta-perfis]] — Veja também: Colima: dimensionamento de CPU, memória, expansão de disco, Rosetta 2 (`--vz-rosetta`) e múltiplos perfis.

## Fontes
- [Colima GitHub — README.md (Docker, Containerd, Kubernetes & Incus Runtimes on macOS/Linux, GPU AI Workloads with krunkit & VM Customization)](https://raw.githubusercontent.com/abiosoft/colima/main/README.md) — README oficial do abiosoft/colima detalhando os runtimes suportados, compartilhamento de imagens com Kubernetes, execução de modelos de IA acelerados por GPU via krunkit e dimensionamento de VM; consultado em 2026-10-03.
- [Colima Official Documentation — docs/FAQ.md (COLIMA_HOME Precedence, colima.yaml Configuration, Docker/Containerd Overrides, Reachable IP & Provision Scripts)](https://raw.githubusercontent.com/abiosoft/colima/main/docs/FAQ.md) — FAQ técnico oficial do Colima cobrindo precedência de diretórios de configuração, customização de daemon.json, múltiplos perfis, endereço IP roteável e scripts de provisionamento; consultado em 2026-10-03.
- [Colima — Official GitHub Repository](https://github.com/abiosoft/colima) — Repositório oficial MIT do Colima; consultado em 2026-10-03.
