---
id: software.devops.tranche06.000557
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/GoogleContainerTools/kaniko/main/README.md", "https://github.com/GoogleContainerTools/kaniko/blob/main/docs/tutorial.md", "https://github.com/GoogleContainerTools/kaniko"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Configuração de autenticação do Kaniko para Docker Hub, Google GCR, Amazon ECR, Azure ACR e JFrog

## Em uma frase
A seção *Pushing to Different Registries* do README oficial explica que o Kaniko utiliza *Docker credential helpers* e arquivos montados em **`/kaniko/.docker/config.json`** para autenticar o push da imagem final nos diferentes registros do mercado: para o **Docker Hub**, monta-se um `config.json` contendo a string `USER:PASSWORD` em base64 sob a chave `"https://index.docker.io/v1/"`; para o **Google GCR / Artifact Registry**, pode-se usar `GOOGLE_APPLICATION_CREDENTIALS` apontando para o Secret JSON ou **Workload Identity** no GKE; e para **Amazon ECR**, **Azure Container Registry (ACR)** e **JFrog Artifactory**, utilizam-se os respectivos helpers de credenciais já incluídos ou credenciais no `config.json`.

## Por que importa
Erros de autenticação no final de um build demorado (quando o Kaniko já compilou todas as camadas e falha apenas na hora do push por um `config.json` montado no caminho errado) são uma das falhas operacionais mais comuns em pipelines Kubernetes.

## Como funciona
Monte sempre o `Secret` do Kubernetes do tipo `kubernetes.io/dockerconfigjson` (ou arquivo `config.json`) exatamente no diretório **`/kaniko/.docker/config.json`** (já que `HOME` dentro do executor Kaniko é protegido em `/kaniko`), e no Docker Hub utilize o endpoint `"https://index.docker.io/v1/"` conforme nota explícita do README.

## Exemplo
Em um cluster Kubernetes, a equipe cria um Secret com as credenciais do registro privado e o monta em `/kaniko/.docker/config.json` como somente-leitura (`readOnly: true`), permitindo que o Kaniko autentique tanto o pull de imagens base privadas quanto o push de `--destination`.

## Limites e trade-offs
Não passe a flag `--skip-push-permission-check` a menos que necessário: por padrão, o Kaniko verifica a permissão de push no registro logo no início do build para falhar rápido caso a credencial em `/kaniko/.docker/config.json` esteja inválida, antes de gastar minutos compilando.

## Como verificar
Execute um build de teste apontando para um repositório autenticado e confirme nos logs a validação inicial de permissão e o push final bem-sucedido.

## Conexões
- [[kaniko-running-kaniko-in-kubernetes-and-gvisor-sandbox]] — Veja também: Execução segura do Kaniko em clusters Kubernetes e dentro do sandbox gVisor (runsc --force).
- [[kaniko-reproducible-builds-digest-files-and-no-push-validation]] — Veja também: Builds reprodutíveis (--reproducible), captura de digests (--digest-file) e validação sem push (--no-push, --tar-path).

## Fontes
- [Kaniko GitHub — README.md (Archival Notice, Userspace Dockerfile Execution, Build Contexts, Caching & Known Issues)](https://raw.githubusercontent.com/GoogleContainerTools/kaniko/main/README.md) — README oficial do Kaniko (GoogleContainerTools/kaniko) registrando o aviso no topo de que o projeto está arquivado e não é mais mantido, seu funcionamento por extração do rootfs e snapshotting em userspace sem daemon Docker dentro de gcr.io/kaniko-project/executor, os 7 contextos de build suportados, cache de camadas (--cache, --cache-repo) e cache de imagens base (gcr.io/kaniko-project/warmer), execução em Kubernetes/gVisor e limitações conhecidas.; consultado em 2026-10-03.
- [Kaniko GitHub — Getting Started Tutorial (docs/tutorial.md)](https://github.com/GoogleContainerTools/kaniko/blob/main/docs/tutorial.md) — Tutorial histórico oficial de uso do Kaniko em clusters Kubernetes.; consultado em 2026-10-03.
- [Kaniko — Official GitHub Repository (Archived)](https://github.com/GoogleContainerTools/kaniko) — Repositório oficial Apache-2.0 arquivado do Kaniko em GoogleContainerTools.; consultado em 2026-10-03.
