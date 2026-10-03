---
id: software.devops.tranche20.001910
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md"
fontes: ["https://raw.githubusercontent.com/linuxkit/linuxkit/master/README.md", "https://raw.githubusercontent.com/linuxkit/linuxkit/master/docs/yaml.md", "https://github.com/linuxkit/linuxkit"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# LinuxKit Image Cache e Testes de Regressão (`rtf`): cache local de imagens OCI e automação de testes de SO

## Em uma frase
O LinuxKit mantém um **cache local em formato OCI** (`~/.linuxkit/cache`) para todos os componentes baixados por `linuxkit build` ou construídos por `linuxkit pkg build`, e utiliza o **Regression Test Framework (`rtf`)** para validar imagens de sistema operacional completas em pipelines de CI.

## Por que importa
Testar uma distribuição Linux customizada exige inicializar a imagem real em um hipervisor, aguardar o kernel e os containers de sistema subirem e executar asserções automatizadas sobre rede, armazenamento e módulos do kernel.

## Como funciona
O comando `linuxkit cache ls` lista todas as imagens e arquiteturas presentes no cache local do LinuxKit (`linuxkit cache clean` limpa o cache). Já a suíte de testes com `rtf` (`rtf -v run -x` ou `rtf -v -l slow run -x`) filtra testes por labels ou padrões (`linuxkit.examples`) e grava os artefatos de log e resultado no diretório `_results`.

## Exemplo
```bash
# Inspecionando o cache local de imagens OCI do LinuxKit:
linuxkit cache ls

# Executando testes de regressão de exemplos com o Regression Test Framework (rtf):
rtf -v run -x linuxkit.examples
```

## Limites e trade-offs
O `linuxkit build` consulta primeiro o cache local (`~/.linuxkit/cache`) antes de buscar imagens em registries remotos, permitindo construir imagens LinuxKit offline uma vez que os pacotes necessários tenham sido cacheados.

## Como verificar
Execute `linuxkit cache ls` após rodar um `linuxkit build` para confirmar os digests e arquiteturas armazenados localmente.

## Conexões
- [[linuxkit-onshutdown-desligamento-limpo-deregister-crash-only-design]] — Veja também: LinuxKit `onshutdown` e *Crash-Only Software*: execução de containers de desligamento limpo e limites operacionais.

## Fontes
- [LinuxKit GitHub — README.md (Toolkit for Building Secure, Portable and Lean Operating Systems for Containers)](https://raw.githubusercontent.com/linuxkit/linuxkit/master/README.md) — README oficial do linuxkit/linuxkit apresentando a arquitetura de imagens de SO imutáveis, formatos de saída, plataformas de execução e ferramentas; consultado em 2026-10-03.
- [LinuxKit Official Documentation — YAML Specification (docs/yaml.md: kernel, init, volumes, onboot, onshutdown, services & files)](https://raw.githubusercontent.com/linuxkit/linuxkit/master/docs/yaml.md) — Especificação oficial YAML do LinuxKit detalhando a ordem de inicialização, alocação simbólica de uid/gid, volumes OCI e configuração runtime; consultado em 2026-10-03.
- [LinuxKit — Official GitHub Repository](https://github.com/linuxkit/linuxkit) — Repositório oficial Apache-2.0 do LinuxKit; consultado em 2026-10-03.
