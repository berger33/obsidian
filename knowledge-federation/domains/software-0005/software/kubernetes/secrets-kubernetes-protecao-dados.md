---
id: software.kubernetes.secrets-boas-praticas.000001
tipo: tecnica
dominio: software
subdominio: kubernetes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: aprovada
revisor: usuario-da-sessao
data_revisao_humana: 2026-10-02
fontes: ["https://kubernetes.io/docs/concepts/security/secrets-good-practices/", "https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/"]
tags: [dominio/software, subdominio/kubernetes, qualidade/candidata]
aliases: [Kubernetes Secret, Secrets management, Kubernetes Secret encryption]
lote: software-kubernetes-operacao-0005
---

# Proteção de Secrets no Kubernetes

## Em uma frase
Um objeto Secret organiza dados confidenciais para uso por Pods, mas sua existência não os cifra automaticamente nem substitui controles de acesso.

## Por que importa
Senhas, tokens e chaves podem vazar por manifests versionados, permissões amplas, logs ou acesso excessivo aos Pods. O tipo `Secret` permite separar dados sensíveis de configuração não confidencial e aplicar controles específicos, mas quem consegue ler o objeto ou executar um Pod que o consome pode potencialmente obter o valor.

## Como funciona
Os valores de Secret aparecem codificados em Base64 na API e, por padrão, são armazenados sem criptografia no etcd. Base64 é codificação, não confidencialidade. Administradores podem configurar criptografia em repouso para dados da API. A documentação recomenda acesso de menor privilégio: limitar `get`, `list` e `watch`, lembrando que `list` permite obter o conteúdo; montar cada Secret apenas nos containers que precisam dele; e proteger o valor depois que a aplicação o lê, por exemplo evitando colocá-lo em logs. ConfigMaps destinam-se a configuração não confidencial.

## Exemplo
Uma aplicação precisa de um token para conectar a um serviço. O Secret fica fora do repositório de manifests públicos, o cluster cifra dados em repouso, apenas a identidade de implantação e a aplicação necessária recebem permissões e o volume é montado somente no container consumidor. Uma solução externa de segredos pode ser adequada quando o ciclo de vida exige rotação ou armazenamento fora do cluster.

## Limites e trade-offs
Criptografia em repouso não impede exposição a workloads autorizados nem corrige permissões excessivas. Restringir leitura direta do objeto não basta se uma identidade pode criar Pods arbitrários que montam o Secret. A política de auditoria, backup, rotação e provedor de armazenamento varia por cluster. Esta nota não prescreve um operador externo específico.

## Como verificar
Revise a configuração do API server e confirme, em armazenamento controlado, que Secrets são cifrados em repouso. Audite RBAC para `get/list/watch`, verifique quais service accounts podem criar Pods e quais containers montam cada Secret. Procure valores reais em Git, logs e outputs de CI; teste rotação e revogação.

## Conexões
- [[rbac-kubernetes-serviceaccounts]] — RBAC determina quais identidades podem ler ou usar Secrets.
- [[networkpolicy-kubernetes-isolamento]] — controle de rede complementa, mas não substitui, a proteção do dado.
- Pipelines CI/CD também precisam de controles próprios para evitar exposição de credenciais.

## Fontes
- [Kubernetes — Good practices for Secrets](https://kubernetes.io/docs/concepts/security/secrets-good-practices/) — Base64, criptografia em repouso, RBAC e exposição por Pods; acesso em 2026-10-01.
- [Kubernetes — Encrypting Confidential Data at Rest](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/) — configuração e validação da criptografia de recursos da API; acesso em 2026-10-01.
