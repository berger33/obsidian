---
id: software.devops.tranche08.000800
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/earthly/earthly/main/README.md", "https://docs.earthly.dev/docs/earthfile", "https://github.com/earthly/earthly"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Earthly: camada agnóstica sobre qualquer CI (GitHub Actions, GitLab CI, CircleCI, Jenkins, Tekton) e modo interativo de debug (-i)

## Em uma frase
O Earthly não substitui o sistema de CI existente, mas roda no topo de qualquer CI (Jenkins, CircleCI, GitHub Actions, GitLab CI, AWS CodeBuild, Tekton), reduzindo o YAML proprietário do CI a uma única chamada `earthly --ci +all` e oferecendo shell interativo (`earthly -i`) quando um passo falha localmente.

## Por que importa
Quando uma empresa codifica toda a sua lógica de build em 500 linhas de YAML específico do GitHub Actions ou Groovy do Jenkins, torna-se impossível rodar esse pipeline localmente no laptop do engenheiro e caríssimo migrar de provedor de CI (vendor lock-in). Segundo a seção `Works With Every Language, Framework and Build Tool` e `Why Earthly` do README oficial, o Earthly desacopla a lógica de build da plataforma de CI.

## Como funciona
Em vez de manter dezenas de steps específicos do provedor no arquivo `.github/workflows/ci.yml` ou `.gitlab-ci.yml`, toda a lógica de dependências, geração de código, lint, testes e empacotamento fica no **`Earthfile`** do repositório, que serve como **contrato único compartilhado** entre a máquina do desenvolvedor e o CI. No servidor de CI, o workflow apenas instala o binário `earthly` e executa **`earthly --ci +target`** (onde `--ci` ativa configurações ideais para integração contínua, como desabilitar salvamento de artefatos locais desnecessários e exigir que tudo esteja limpo). Localmente, se um comando `RUN` falhar, o desenvolvedor pode executar **`earthly -i +target`** (`--interactive`) para cair automaticamente em um shell interativo dentro do container no exato instante da falha para inspecionar o problema.

## Exemplo
```bash
# Executar o target no servidor de integração contínua (--ci) vs abrir shell interativo (-i) em caso de falha local
earthly --ci +all
earthly -i +test
```

## Limites e trade-offs
Em runners de CI efêmeros (onde a máquina virtual do GitHub Actions ou GitLab CI começa com o disco vazio a cada execução), o container `earthly-buildkitd` inicia sem cache local de camadas; para preservar o cache do BuildKit entre diferentes execuções de CI, configure o cache remoto do Earthly (`--remote-cache <image>` em um registry OCI) ou volumes persistentes no runner auto-hospedado.

## Como verificar
Compare a execução de `earthly +all` na sua máquina local com `earthly --ci +all` no pipeline de CI e confirme que ambas executam exatamente os mesmos containers e versões de ferramentas definidos no `Earthfile`.

## Conexões
- [[earthly-execucao-paralela-dag-buildkit-cache-camadas]] — Veja também: Earthly: paralelismo automático por DAG no BuildKit, mounts de cache (--mount type=cache) e funções reutilizáveis (FUNCTION).
- [[earthly-automacao-build-containers-earthfile-reprodutivel]] — Referência cruzada direta com earthly-automacao-build-containers-earthfile-reprodutivel.
- [[earthly-sintaxe-earthfile-targets-dependencias-build]] — Referência cruzada direta com earthly-sintaxe-earthfile-targets-dependencias-build.

## Fontes
- [Earthly GitHub — README.md (Containerized Build Framework, Earthfile Examples, Cross-Directory Imports, Multi-Platform & Secrets)](https://raw.githubusercontent.com/earthly/earthly/main/README.md) — README oficial do Earthly (MPL-2.0) demonstrando sintaxe Earthfile VERSION 0.8, SAVE ARTIFACT AS LOCAL, SAVE IMAGE, FROM DOCKERFILE, imports entre diretórios/repositórios, builds multiplataforma e RUN --push --secret; consultado em 2026-10-03.
- [Earthly Official Documentation — Earthfile Reference](https://docs.earthly.dev/docs/earthfile) — Referência técnica oficial da gramática do Earthfile, base target, invocação de targets (+), WITH DOCKER, CACHE e FUNCTION; consultado em 2026-10-03.
- [Earthly — Official GitHub Repository](https://github.com/earthly/earthly) — Repositório oficial MPL-2.0 do Earthly; consultado em 2026-10-03.
