---
id: software.devops.tranche08.000793
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

# Earthly: exportação de artefatos entre targets e para o host (SAVE ARTIFACT ... AS LOCAL) e imagens (SAVE IMAGE)

## Em uma frase
O Earthly utiliza `SAVE ARTIFACT` para expor arquivos gerados dentro de um target para outros targets (`COPY +target/artefato`) ou diretamente para o sistema de arquivos da máquina host (`AS LOCAL`), e `SAVE IMAGE` para exportar imagens de container para o daemon local ou registries (`--push`).

## Por que importa
Em um `Dockerfile` comum, extrair um binário compilado, um relatório de cobertura de testes ou código gerado por `protoc` de dentro de uma etapa intermediária de build para a pasta local do desenvolvedor exige truques manuais com `docker create` + `docker cp` ou flags complexas do `buildx --output`. Na especificação do `Earthfile`, `SAVE ARTIFACT ... AS LOCAL` e `SAVE IMAGE` tornam as saídas cidadãs de primeira classe.

## Como funciona
(1) **`SAVE ARTIFACT <src> [<dest-artifact>] [AS LOCAL <local-path>]`**: marca um arquivo ou diretório produzido pelo target como artefato exportado; qualquer outro target (no mesmo `Earthfile`, em outro diretório ou em outro repositório Git) pode copiá-lo usando `COPY +<target>/<dest-artifact> <destino>`. Se a cláusula `AS LOCAL <local-path>` for incluída e o target fizer parte da cadeia diretamente solicitada pelo usuário, o Earthly grava o arquivo diretamente no disco do host ao final do build com sucesso; e (2) **`SAVE IMAGE [--push] <image-name>:<tag>`**: salva o estado final do sistema de arquivos e metadados (`ENTRYPOINT`, `CMD`, `ENV`, `EXPOSE`) do target como uma imagem Docker local, publicando-a no registry remoto se `--push` for passado na CLI (`earthly --push +docker`).

## Exemplo
```bash
# Executar o target +build que contém SAVE ARTIFACT build/go-example AS LOCAL build/go-example
earthly +build
ls -lh build/go-example
```

## Limites e trade-offs
O Earthly só transfere artefatos `AS LOCAL` e imagens `SAVE IMAGE` para o host (e só executa comandos marcados com `--push`) depois que **todos** os passos do grafo de build solicitado terminam com sucesso; se um target `+test` incluído em `earthly +all` falhar, nenhuma imagem é publicada e nenhum artefato parcial sobrescreve os arquivos locais do host (atomicidade das saídas de build).

## Como verificar
Execute `earthly +docker` e em seguida `docker images go-example:latest` para confirmar que a imagem definida em `SAVE IMAGE` foi carregada no daemon de containers local.

## Conexões
- [[earthly-sintaxe-earthfile-targets-dependencias-build]] — Veja também: Earthly: estrutura do Earthfile (VERSION 0.8, base target, indentação e invocação de targets com +).
- [[earthly-imports-monorepos-multi-repositorios-remotos]] — Veja também: Earthly: composição de builds em monorepos e entre múltiplos repositórios Git remotos.
- [[earthly-automacao-build-containers-earthfile-reprodutivel]] — Referência cruzada direta com earthly-automacao-build-containers-earthfile-reprodutivel.

## Fontes
- [Earthly GitHub — README.md (Containerized Build Framework, Earthfile Examples, Cross-Directory Imports, Multi-Platform & Secrets)](https://raw.githubusercontent.com/earthly/earthly/main/README.md) — README oficial do Earthly (MPL-2.0) demonstrando sintaxe Earthfile VERSION 0.8, SAVE ARTIFACT AS LOCAL, SAVE IMAGE, FROM DOCKERFILE, imports entre diretórios/repositórios, builds multiplataforma e RUN --push --secret; consultado em 2026-10-03.
- [Earthly Official Documentation — Earthfile Reference](https://docs.earthly.dev/docs/earthfile) — Referência técnica oficial da gramática do Earthfile, base target, invocação de targets (+), WITH DOCKER, CACHE e FUNCTION; consultado em 2026-10-03.
- [Earthly — Official GitHub Repository](https://github.com/earthly/earthly) — Repositório oficial MPL-2.0 do Earthly; consultado em 2026-10-03.
