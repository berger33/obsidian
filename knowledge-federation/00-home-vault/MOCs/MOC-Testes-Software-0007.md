# MOC — Testes de Software (lote 0007)

Índice das 1759 notas substantivas redigidas até agora no lote `software-testes-2000-0001`, cuja meta é 2.000. As 1759 passaram pelo gate automatizado e têm revisão factual registrada: nove aprovadas pelo usuário e 1750 aprovadas por IA, sem converter estas últimas em aprovações humanas. Este mapa é navegação, não validação factual.

## Fundamentos, processo e testware
- [[test-objectives-context]] — selecionar objetivos conforme work product, riscos e contexto.
- [[testing-principles-contextual]] — usar os sete princípios como orientação contextual.
- [[error-defect-failure-root-cause]] — distinguir erro, defeito, falha e causa raiz.
- [[testing-vs-debugging]] — separar evidência de teste da investigação/correção.
- [[fundamental-test-activities]] — planejar, analisar, desenhar, implementar, executar e concluir.
- [[test-process-context-tailoring]] — adaptar atividades à situação, sem adotar receita única.
- [[testing-roles-management-and-testing]] — distinguir responsabilidades de gestão e função técnica.
- [[testware-artifacts]] — organizar os produtos de trabalho gerados pelas atividades.

## Teste estático, feedback e revisões
- [[static-testing-work-products]] — revisar work products e aplicar análise estática sem execução.
- [[static-vs-dynamic-testing]] — combinar evidências de abordagens complementares.
- [[early-frequent-stakeholder-feedback]] — obter feedback de stakeholders ao longo do SDLC.
- [[review-process-activities]] — estruturar planejamento, leitura, comunicação e tratamento de findings.
- [[review-types-formality-purpose]] — selecionar tipo de revisão conforme objetivo e risco.
- [[review-success-factors]] — preparar participantes e medir sucesso sem avaliar indivíduos.

## Níveis de teste
- [[test-levels-overview]] — comparar os cinco níveis do CTFL e seus objetivos.
- [[component-testing-isolation]] — avaliar componentes isolados.
- [[component-integration-testing-interfaces]] — examinar interações entre componentes.
- [[system-testing-requirements]] — verificar comportamento do sistema integrado.
- [[system-integration-testing-external-systems]] — testar interfaces com sistemas/serviços externos.
- [[acceptance-testing-validation]] — validar necessidades e readiness para uso/implantação.

## SDLC, manutenção e tipos de teste
- [[sdlc-impact-on-testing]] — relaciona o ciclo de vida ao escopo, timing e abordagem.
- [[testing-sequential-and-iterative-sdlc]] — compara cadência e sobreposição das atividades.
- [[good-testing-practices-across-sdlc]] — práticas de teste úteis em vários modelos.
- [[test-first-approaches-tdd-atdd-bdd]] — situa TDD, ATDD e BDD.
- [[test-driven-development]] — orienta código por testes escritos antes.
- [[acceptance-test-driven-development]] — deriva casos de critérios de aceitação.
- [[behavior-driven-development]] — comunica comportamento com exemplos.
- [[devops-testing-continuous-feedback]] — aproxima desenvolvimento, teste e operação.
- [[shift-left-testing]] — antecipa verificação sem retirar testes posteriores.
- [[testing-retrospectives-process-improvement]] — transforma experiência em melhorias acompanhadas.
- [[maintenance-testing-change-scope]] — considera risco e tamanho da mudança.
- [[maintenance-testing-triggers]] — cobre modificações, migrações e aposentadoria.
- [[testing-migrations-and-platform-upgrades]] — verifica ambiente e conversão de dados.
- [[retirement-testing-data-archival]] — valida arquivamento e recuperação.
- [[independence-of-testing-levels]] — compara níveis de independência.
- [[whole-team-approach-quality]] — compartilha responsabilidade quando apropriado.
- [[essential-skills-for-testers]] — mapeia competências para o trabalho de teste.
- [[functional-testing-quality-characteristics]] — verifica o que o sistema faz.
- [[nonfunctional-testing-quality-attributes]] — avalia como o sistema se comporta.
- [[confirmation-testing-after-fix]] — confirma correções.
- [[regression-testing-change-effects]] — identifica efeitos colaterais de mudanças.
- [[black-box-testing-specification-based]] — deriva testes da especificação.
- [[white-box-testing-structure-and-limits]] — usa a estrutura interna como base.
- [[experience-based-testing-techniques]] — organiza técnicas baseadas em experiência.
- [[error-guessing-experience]] — formula hipóteses a partir do histórico.
- [[checklist-based-testing]] — mantém condições focadas em uma lista.
- [[collaboration-based-test-approach]] — usa conversa para evitar defeitos.
- [[user-story-three-cs]] — organiza Card, Conversation e Confirmation.
- [[acceptance-criteria-as-test-conditions]] — trata critérios como condições testáveis.

## Papéis de revisão e suporte de ferramentas
- [[review-roles-responsibilities]] — distribui tarefas entre papéis da revisão.
- [[review-moderator-facilitator]] — facilita reuniões construtivas.
- [[review-scribe-recorder]] — registra findings e decisões.
- [[review-reviewer-role]] — examina work products e descreve anomalias.
- [[review-author-feedback-correction]] — cria e corrige o material revisado.
- [[review-leader-responsibility]] — responde pela organização geral.
- [[review-manager-resources]] — define prioridade e disponibiliza recursos.
- [[review-role-allocation-context]] — adapta a alocação ao risco e à formalidade.
- [[test-tool-categories]] — organiza categorias por atividade apoiada.
- [[test-tools-beyond-automation]] — inclui gestão, revisão e colaboração.
- [[test-tool-introduction-and-risk]] — planeja adoção, treinamento e mitigação.

## Isolamento, confiabilidade e regressão
- [[test-doubles-fakes-stubs-spies-mocks]] — escolher doubles conforme o papel e a forma de verificação.
- [[testes-hermeticos-dependencias]] — controlar e declarar dependências do ambiente.
- [[testes-flaky-determinismo]] — diagnosticar resultados inconsistentes.
- [[fixtures-pytest-ciclo-vida-escopos]] — controlar preparação, escopo e limpeza no pytest.
- [[snapshot-testing-jest-revisao]] — detectar mudanças de saída com snapshots revisados.
- [[regression-test-prioritization-risco-impacto]] — ordenar testes de regressão considerando impacto e risco.

## Seleção de dados e combinações
- [[particionamento-equivalencia-valores-fronteira]] — selecionar representantes de classes e exercitar limites.
- [[decision-table-testing-regras-condicionais]] — cobrir regras definidas por combinações de condições.
- [[combinatorial-testing-pairwise-t-way]] — cobrir interações t-way de parâmetros.

## Geração de casos, propriedades e sequências
- [[property-based-testing-hypothesis]] — expressar propriedades sobre entradas geradas.
- [[shrinking-contraexemplos-hypothesis]] — simplificar entradas que reproduzem uma falha.
- [[testes-stateful-model-based-hypothesis]] — gerar sequências de operações sobre sistemas com estado.
- [[state-transition-testing-coverage]] — derivar sequências e critérios de cobertura de modelos de estado.
- [[fuzzing-coverage-guided-libfuzzer]] — explorar caminhos com fuzzing guiado por cobertura.
- [[metamorphic-testing-oracle-relations]] — verificar relações entre execuções sem exigir oracle completo.
- [[differential-testing-comparacao-implementacoes]] — investigar divergências entre implementações equivalentes.
- [[test-oracles-resultados-esperados]] — escolher critérios para avaliar resultados de teste.

## Exploração e gestão de risco
- [[risk-based-testing-priorizacao-risco]] — concentrar esforço nos riscos de maior probabilidade e impacto.
- [[exploratory-testing-aprendizado-design-execucao]] — aprender, projetar e executar testes de forma integrada.
- [[session-based-testing-charters-debriefs]] — estruturar a exploração com missão, relato e debrief.

## Cobertura e eficácia das verificações
- [[cobertura-branches-statement-interpretacao]] — distinguir cobertura de statements e branches.
- [[mcdc-coverage-condicoes-independentes]] — verificar o efeito independente de condições lógicas.
- [[mutation-testing-eficacia-testes]] — verificar se a suíte detecta alterações de comportamento.
- [[piramide-testes-estrategia-contexto]] — distribuir testes conforme risco, custo e arquitetura.

## Acessibilidade, desempenho e resiliência
- [[teste-acessibilidade-automatizada-revisao-humana]] — combinar scanner com avaliação manual de tarefas acessíveis.
- [[performance-testing-modelagem-carga]] — modelar carga e critérios de desempenho.
- [[chaos-experiments-steady-state-blast-radius]] — testar resiliência com hipóteses e impacto controlado.

## Contratos de API e dados
- [[schema-based-api-testing-schemathesis-openapi]] — gerar casos de API a partir de um schema.
- [[test-data-privacidade-sinteticos]] — reduzir exposição e avaliar utilidade de dados de teste.

## Planejamento, controle e governança do teste
- [[test-planning-objetivos-escopo-comunicacao]] — alinhar objetivos, recursos, cronograma e comunicação.
- [[test-entry-exit-criteria]] — definir condições para iniciar e concluir atividades.
- [[test-effort-estimation-techniques]] — estimar esforço com métodos baseados em dados ou especialistas.
- [[test-case-prioritization-dependencies]] — ordenar casos considerando risco, cobertura e dependências.
- [[test-progress-metrics-relatorios-conclusao]] — monitorar resultados e comunicar progresso/encerramento.
- [[test-environment-configuration-management]] — manter versões e contexto reproduzíveis para testware.
- [[requirements-test-traceability]] — ligar base de teste, casos, resultados e defeitos.
- [[defect-report-reproducibility-severity-priority]] — registrar anomalias que possam ser reproduzidas e triadas.
- [[test-automation-investment-maintenance-risks]] — avaliar investimento, ROI e manutenção de automação.
- [[ci-feedback-testes-regressao]] — usar CI para fornecer feedback frequente e controlado.

## Desempenho: perfis de carga, percentis e testes de capacidade
- [[testes-latencia-percentis-thresholds]] — Defina limites de desempenho sobre percentis de latência, taxa de erros e objetivos de serviço, em vez de depender apenas da média.
- [[testes-correcao-funcional-sob-carga]] — Verifique respostas e invariantes funcionais enquanto o sistema atende carga, sem confundir sucesso HTTP isolado com correção do fluxo.
- [[testes-modelagem-carga-vus-taxa-chegada]] — Selecione um modelo aberto ou fechado de geração de carga de acordo com a pergunta que o teste pretende responder.
- [[testes-smoke-carga-minima-api]] — Use uma execução curta e de baixa carga para confirmar que o script, os endpoints principais e o ambiente respondem antes de testes maiores.
- [[testes-carga-media-perfil-trafego]] — Avalie o serviço com um perfil que represente tráfego típico, mix de operações e duração operacional relevante para a decisão.
- [[testes-stress-limite-capacidade]] — Aumente a carga de forma controlada acima do padrão esperado para observar degradação, ponto de saturação e recuperação.
- [[testes-spike-picos-abruptos]] — Simule uma subida rápida de carga para examinar se filas, autoscaling e dependências suportam mudanças abruptas e como o serviço se recupera.
- [[testes-soak-degradacao-temporal]] — Mantenha uma carga representativa por período prolongado para procurar degradação lenta que testes curtos não revelam.
- [[testes-breakpoint-rampa-carga]] — Aumente gradualmente a taxa ou concorrência para localizar a faixa em que o sistema deixa de cumprir critérios operacionais.
- [[testes-canary-validacao-telemetria]] — Use uma parcela controlada de tráfego real para observar se uma versão nova preserva sinais de saúde antes de ampliar o rollout.

## Acessibilidade: critérios WCAG e regressão multimodal
- [[teste-acessibilidade-navegacao-teclado]] — Verifique se ações e conteúdo operáveis podem ser alcançados e acionados sem mouse, respeitando o comportamento esperado de cada controle.
- [[teste-acessibilidade-foco-visivel-ordem]] — Examine se o foco de teclado permanece visível e percorre uma sequência que preserva significado e operabilidade.
- [[teste-acessibilidade-rotulos-erros-formulario]] — Confirme que controles têm rótulos e instruções associados e que erros identificam o campo, o problema e a forma de correção.
- [[teste-acessibilidade-nome-papel-valor]] — Valide se controles nativos e customizados expõem nome acessível, papel e estado coerentes com a função e com a interação atual.
- [[teste-acessibilidade-contraste]] — Meça contraste nas cores efetivamente renderizadas em cada estado relevante e confronte os resultados com o critério WCAG aplicável.
- [[teste-acessibilidade-reflow-zoom]] — Avalie se conteúdo e funcionalidade permanecem disponíveis quando o viewport é estreito ou o usuário amplia o conteúdo, sem exigir rolagem bidimensional indevida.
- [[teste-acessibilidade-wcag-target-size]] — Meça os alvos de entrada por ponteiro e avalie o requisito mínimo de tamanho ou as exceções de espaçamento definidas no critério.
- [[teste-acessibilidade-autenticacao-acessivel]] — Verifique se o processo de autenticação evita exigir uma função cognitiva sem alternativa ou apoio permitido pelo critério de acessibilidade aplicável.
- [[teste-acessibilidade-status-dinamico]] — Confirme que mensagens de sucesso, erro, progresso ou resultado de ação são programaticamente determináveis sem depender de uma mudança de foco.
- [[teste-acessibilidade-regressao-multimodal]] — Combine verificações automatizadas repetíveis com percursos manuais de teclado, zoom e tecnologia assistiva para detectar regressões de acesso.

## Segurança: autorização, sessão, entrada, headers e logs
- [[testes-autorizacao-horizontal-objetos]] — Verifique se uma conta autenticada consegue ler ou alterar somente os objetos pertencentes ao seu próprio escopo.
- [[testes-autorizacao-vertical-privilegios]] — Avalie se usuários de menor privilégio são impedidos de executar funções reservadas a papéis superiores, inclusive por chamadas diretas.
- [[testes-sessao-idle-timeout-replay]] — Verifique se a sessão expira por inatividade conforme a política e se um identificador invalidado não volta a autorizar requisições.
- [[testes-session-fixation-regeneracao-id]] — Confirme que uma sessão pré-autenticação não conserva o mesmo identificador depois que a identidade ou o privilégio da conta muda.
- [[testes-csrf-origem-token-cookie]] — Examine se uma operação que altera estado rejeita solicitações cross-site não autorizadas e se proteções são avaliadas no contexto real dos cookies.
- [[testes-validacao-input-reflected-xss]] — Siga entradas controladas até o contexto de saída e verifique se texto não confiável é exibido como dado, sem execução de conteúdo ativo.
- [[testes-ssrf-destino-url-egress]] — Avalie se uma funcionalidade que busca URLs limita destinos e protocolos a uma política explícita, sem alcançar recursos internos não autorizados.
- [[testes-autenticacao-rate-limit-enumeracao]] — Verifique que tentativas automatizadas são limitadas sem expor a existência de contas nem permitir que um teste cause bloqueio de usuários reais.
- [[testes-security-headers-browser]] — Inspecione cabeçalhos emitidos em respostas relevantes e valide se sua política corresponde à arquitetura e ao comportamento esperado do navegador.
- [[testes-logs-redaction-injection]] — Verifique que eventos necessários são registrados, dados secretos são excluídos ou mascarados e entradas não confiáveis não forjam registros.

## Confiabilidade, recuperação e rollout
- [[testes-degradacao-graciosa-invariantes]] — Introduza indisponibilidade ou lentidão de uma dependência e verifique se o serviço preserva operações essenciais ou comunica uma falha controlada.
- [[testes-load-shedding-limites-sobrecarga]] — Examine se, sob sobrecarga, o sistema limita trabalho e rejeita solicitações de forma controlada antes de comprometer todos os recursos.
- [[testes-retry-backoff-jitter-cascata]] — Valide que novas tentativas são limitadas, espaçadas e seguras para a operação, evitando multiplicar a carga quando uma dependência falha.
- [[testes-falha-dependencia-timeout-circuit-breaker]] — Simule timeout e falha de serviço dependente para confirmar orçamento de espera, abertura do circuit breaker e recuperação controlada.
- [[testes-restore-backup-integridade]] — Restaure um backup em ambiente isolado e confirme que dados e serviço podem ser recuperados, não apenas que o arquivo existe.
- [[testes-recuperacao-rto-rpo]] — Meça em exercício controlado se a recuperação atende objetivos declarados de tempo e perda máxima de dados, incluindo dependências necessárias.
- [[testes-canary-comparacao-baseline]] — Compare a versão canário e a versão estável por métricas e resultados sob condições suficientemente semelhantes antes de promover a mudança.
- [[testes-kubernetes-rolling-update-disponibilidade]] — Exercite uma atualização progressiva e confirme estado do Deployment, prontidão dos Pods e continuidade das operações esperadas.
- [[testes-rollback-versao-estado]] — Prove que uma implantação problemática pode ser revertida e que a versão anterior opera com o estado produzido durante a atualização.
- [[testes-probes-startup-liveness-readiness]] — Teste cada probe segundo seu propósito: permitir inicialização, reiniciar processo travado ou retirar temporariamente tráfego de instância não pronta.

## HTTP, contratos e integridade de dados
- [[testes-http-content-negotiation-vary]] — Verifique se o servidor escolhe uma representação compatível com Accept e outras preferências documentadas e se caches distinguem variantes quando necessário.
- [[testes-semantica-metodos-http-idempotencia]] — Verifique que métodos aceitos produzem os efeitos definidos pelo contrato HTTP, incluindo segurança, idempotência e resposta adequada a métodos não permitidos.
- [[testes-api-problem-details-rfc9457]] — Valide que erros publicados com Problem Details respeitam mídia, semântica HTTP e estrutura prevista no contrato, sem expor detalhes internos.
- [[testes-http-conditional-requests-etag]] — Exercite validators e precondições HTTP para detectar cache condicional e conflitos de atualização sem sobrescrever silenciosamente estado concorrente.
- [[testes-pagination-cursor-invariantes]] — Verifique que a navegação por cursor mantém ordem e cobertura previstas no contrato diante de limites, filtros e alterações concorrentes controladas.
- [[testes-api-rate-limit-429-retry-after]] — Valide a resposta à quota excedida e se clientes e caches respeitam o contrato de limitação de taxa sem retentar de forma agressiva.
- [[testes-contract-testing-compatibilidade-api]] — Combine validação de schema com interações que representam necessidades reais de consumidores para detectar incompatibilidades antes do deploy.
- [[testes-consumer-idempotency-duplicates]] — Entregue a mesma mensagem mais de uma vez e confirme que consumidor produz no máximo o efeito de negócio definido para aquele identificador.
- [[testes-consistencia-eventual-convergencia]] — Verifique se leituras eventualmente consistentes convergem dentro do comportamento e prazo operacional declarados, sem exigir visibilidade imediata não prometida.
- [[testes-database-integrity-reconciliation]] — Verifique invariantes de dados tanto no limite transacional do banco quanto em reconciliações independentes entre fontes ou projeções.

## Tranche 8 — frameworks e plataformas de teste (100 notas)

### Playwright
- [[playwright-fixture-ciclo-vida-isolamento]] — Playwright: ciclo de vida de fixtures por teste.
- [[playwright-fixture-worker-escopo-paralelismo]] — Playwright: fixtures de worker e estado compartilhado.
- [[playwright-autenticacao-storage-state-expiracao]] — Playwright: reutilização segura de estado autenticado.
- [[playwright-teardown-recursos-externos]] — Playwright: teardown confiável de recursos externos.
- [[playwright-mock-api-contrato-resposta]] — Playwright: mocks de API alinhados ao contrato.
- [[playwright-har-replay-cobertura-rede]] — Playwright: replay de HAR para cenários de rede.
- [[playwright-status-http-vs-falha-transporte]] — Playwright: distinguir erro HTTP de falha de transporte.
- [[playwright-retries-flaky-diagnostico]] — Playwright: retries como sinal de flakiness, não correção.
- [[playwright-paralelismo-dados-exclusivos]] — Playwright: dados exclusivos para testes paralelos.
- [[playwright-locators-assertions-web-first]] — Playwright: locators resilientes e assertions web-first.

### React Testing Library
- [[rtl-interacao-user-event-fluxo-realista]] — Testing Library: interações realistas com user-event.
- [[rtl-consultas-prioridade-role-name]] — Testing Library: priorizar consultas por papel e nome.
- [[rtl-async-findby-waitfor-condicao]] — Testing Library: aguardar estado assíncrono pela condição.
- [[rtl-waitfor-sem-efeito-colateral]] — Testing Library: manter waitFor sem efeitos colaterais.
- [[rtl-formulario-erro-associacao-label]] — Testing Library: validar formulários pela relação label-controle.
- [[rtl-render-customizado-provedores-contexto]] — Testing Library: render customizado com provedores.
- [[rtl-testar-resultado-nao-implementacao]] — Testing Library: verificar resultado em vez de detalhe interno.
- [[rtl-consulta-singular-ambiguidade]] — Testing Library: detectar consultas ambíguas.
- [[rtl-fetch-loading-empty-error-states]] — Testing Library: cobrir loading, vazio e erro de carregamento.
- [[rtl-cleanup-isolamento-renderizacao]] — Testing Library: limpeza e isolamento entre renders.

### Android
- [[android-test-pyramid-escopo-runner]] — Android: escolher escopo e runner de teste.
- [[android-instrumented-sincronizacao-sem-sleep]] — Android: sincronizar testes instrumentados sem sleeps fixos.
- [[android-uiautomator-fronteira-sistema]] — Android: UI Automator para fronteiras de sistema.
- [[android-compose-semantics-assertions]] — Android Compose: testar semântica e ações expostas.
- [[android-compose-clock-idle-animacoes]] — Android Compose: controlar clock e animações em testes.
- [[android-multiplas-telas-configuracao]] — Android: cobrir tamanhos de tela e configuração.
- [[android-process-death-restauracao-estado]] — Android: testar restauração após recriação do processo.
- [[android-permissoes-recusa-revocacao]] — Android: testar concessão, recusa e revogação de permissões.
- [[android-separar-teste-ui-de-regra]] — Android: não concentrar regras de negócio em teste de UI.
- [[android-test-flakiness-reproducao-dispositivo]] — Android: tornar falhas instrumentadas reproduzíveis.

### Flutter
- [[flutter-estrategia-unit-widget-integration]] — Flutter: distribuir testes entre unit, widget e integração.
- [[flutter-plugin-channel-mock-fronteira]] — Flutter: mockar canais de plugin sem alegar teste nativo.
- [[flutter-integration-dispositivo-fluxo]] — Flutter: desenhar testes de integração em dispositivo.
- [[flutter-widget-lista-rolagem-scrolluntilvisible]] — Flutter: testar listas longas sem assumir posição fixa.
- [[flutter-orientacao-layout-widget-test]] — Flutter: validar orientação retrato e paisagem.
- [[flutter-pumpandsettle-animacao-indefinida]] — Flutter: evitar pumpAndSettle em animações sem fim.
- [[flutter-finders-chaves-vs-texto]] — Flutter: escolher Finder por semântica, texto ou chave.
- [[flutter-testwidgets-pump-microtasks]] — Flutter: sincronizar pump e atualizações assíncronas.
- [[flutter-widget-erro-overflow-responsivo]] — Flutter: detectar overflow e conteúdo inacessível em widget tests.
- [[flutter-mocks-plugin-versus-device-regressao]] — Flutter: separar contrato simulado de regressão em dispositivo.

### Terraform
- [[terraform-validate-vs-test-provisionamento]] — Terraform: distinguir validate de terraform test.
- [[terraform-tests-mock-provider-escopo]] — Terraform: delimitar mocks de provider.
- [[terraform-test-run-apply-cleanup]] — Terraform: isolar testes que aplicam infraestrutura.
- [[terraform-variable-validation-contract]] — Terraform: testar validação de variáveis como contrato.
- [[terraform-check-block-nao-blocking]] — Terraform: interpretar check blocks sem tratá-los como preconditions.
- [[terraform-outputs-sensitive-testes]] — Terraform: testar outputs sem expor valores sensíveis.
- [[terraform-provider-lockfile-reprodutibilidade]] — Terraform: validar reprodutibilidade de providers.
- [[terraform-data-sources-outputs-mock-real]] — Terraform: testar data sources e outputs calculados.
- [[terraform-plan-assertions-estado-esperado]] — Terraform: verificar plano contra mudança de infraestrutura esperada.
- [[terraform-sandbox-isolamento-paralelo]] — Terraform: isolar sandboxes de testes paralelos.

### Kafka
- [[kafka-producer-idempotencia-retries-acks]] — Kafka: testar produtor idempotente e confirmação.
- [[kafka-ordering-partition-retries]] — Kafka: delimitar ordenação por partição.
- [[kafka-transactional-producer-consumer-read-committed]] — Kafka: testar transações com consumidor read-committed.
- [[kafka-offset-commit-proximo-registro]] — Kafka: verificar semântica de offset committed.
- [[kafka-at-least-once-consumidor-idempotente]] — Kafka: tornar efeitos do consumidor seguros contra redelivery.
- [[kafka-rebalance-processamento-em-curso]] — Kafka: testar rebalance com processamento em andamento.
- [[kafka-retry-dlq-erro-transitorio-permanente]] — Kafka: separar erro transitório de erro permanente.
- [[kafka-producer-callback-delivery-failure]] — Kafka: observar falhas de entrega no produtor.
- [[kafka-consumer-reset-start-offset]] — Kafka: testar offset inicial e política de reset.
- [[kafka-testcontainers-contrato-broker]] — Kafka: escolher broker de teste conforme contrato.

### Machine learning
- [[ml-feature-schema-contract-validacao]] — ML: validar schema de features antes do serving.
- [[ml-training-serving-skew-transformacao]] — ML: detectar divergência entre transformação de treino e serving.
- [[ml-data-leakage-split-temporal]] — ML: testar vazamento de informação entre splits.
- [[ml-reproducibilidade-seed-ambiente-artefatos]] — ML: tornar experimentos e artefatos reproduzíveis.
- [[ml-calibracao-limiares-decisao]] — ML: testar calibração e limiares de decisão.
- [[ml-monitoring-drift-feature-label]] — ML: monitorar drift sem confundir com queda de qualidade.
- [[ml-batch-online-paridade-predicoes]] — ML: comparar predição batch e online.
- [[ml-model-serving-fallback-timeout]] — ML: testar timeout e fallback de serving.
- [[ml-numerica-tolerancia-estabilidade]] — ML: definir tolerância para comparações numéricas.
- [[ml-canary-release-rollback-metricas]] — ML: liberar modelo por canário e critério de rollback.

### GitHub Actions
- [[gha-minimum-token-permissions]] — GitHub Actions: limitar permissões do token GITHUB_TOKEN.
- [[gha-script-injection-event-context]] — GitHub Actions: evitar injeção em scripts com contexto de evento.
- [[gha-pinning-third-party-actions]] — GitHub Actions: fixar e revisar actions de terceiros.
- [[gha-secrets-pull-request-forks]] — GitHub Actions: proteger secrets em pull requests externos.
- [[gha-concurrency-cancel-deployments]] — GitHub Actions: configurar concurrency sem cancelar release válida.
- [[gha-artifact-retention-provenance]] — GitHub Actions: reter artifacts sem perder proveniência.
- [[gha-environment-protection-gates]] — GitHub Actions: verificar gates de environment antes do deploy.
- [[gha-matrix-fail-fast-coverage]] — GitHub Actions: desenhar matrix que detecta incompatibilidade.
- [[gha-job-output-untrusted-artifacts]] — GitHub Actions: não confiar em artifacts de execução não privilegiada.
- [[gha-path-filters-ci-cobertura]] — GitHub Actions: testar path filters e caminhos de validação.

### Prometheus
- [[prometheus-alert-rule-unit-test-input-series]] — Prometheus: testar alert rules com séries controladas.
- [[prometheus-alert-for-pending-firing]] — Prometheus: cobrir estados pending e firing de alertas.
- [[prometheus-alert-labels-annotations-invariantes]] — Prometheus: validar labels e annotations de alertas.
- [[prometheus-recording-rule-expression-output]] — Prometheus: testar recording rules e série resultante.
- [[prometheus-rate-counter-reset]] — Prometheus: testar rate diante de reset de counter.
- [[prometheus-vector-vazio-vs-zero]] — Prometheus: diferenciar vetor vazio de valor zero.
- [[prometheus-aggregation-labels-cardinality]] — Prometheus: testar agregação e preservação de labels.
- [[prometheus-alert-no-data-scrape-failure]] — Prometheus: separar condição saudável de ausência de telemetria.
- [[prometheus-rule-test-boundary-time-window]] — Prometheus: cobrir fronteiras de janela em testes de regras.
- [[prometheus-promtool-ci-rule-validation]] — Prometheus: executar promtool no CI para regras versionadas.

### Docker
- [[docker-build-context-dockerignore-audit]] — Docker: auditar build context e .dockerignore.
- [[docker-multistage-runtime-minimo]] — Docker: verificar fronteira entre build stage e runtime.
- [[docker-base-image-digest-atualizacao]] — Docker: controlar base image e processo de atualização.
- [[docker-build-checks-lint-dockerfile]] — Docker: executar build checks para detectar erros de Dockerfile.
- [[docker-build-secrets-nao-arg-env]] — Docker: não inserir secrets em ARG, ENV ou layers.
- [[docker-container-nonroot-permissions]] — Docker: testar execução com usuário não privilegiado.
- [[docker-runtime-healthcheck-supervision]] — Docker: validar healthcheck sem confundi-lo com readiness.
- [[docker-image-test-smoke-entrypoint]] — Docker: testar a imagem final com smoke test.
- [[docker-cache-reproducibilidade-build]] — Docker: testar cache sem depender dele para correção.
- [[docker-image-sbom-provenance-release]] — Docker: associar imagem publicada a versão e proveniência.

## Tranche 9 — frameworks, protocolos e infraestrutura de teste (100 notas)

### Cypress
- [[cypress-test-isolation-indexeddb]] — Cypress: entender o alcance do test isolation.
- [[cypress-query-retry-sem-repetir-efeitos]] — Cypress: distinguir retryability de queries e efeitos.
- [[cypress-intercept-browser-vs-cy-request]] — Cypress: cy.intercept observa tráfego do app, não cy.request.
- [[cypress-register-intercept-before-trigger]] — Cypress: registrar intercept antes da ação que dispara a rede.
- [[cypress-stub-versus-real-server-coverage]] — Cypress: equilibrar stubs de rede e fluxo com servidor real.
- [[cypress-session-cache-validacao]] — Cypress: validar uma sessão restaurada por cy.session.
- [[cypress-cross-origin-cy-origin]] — Cypress: cruzar origens com cy.origin no mesmo teste.
- [[cypress-clock-timers-date]] — Cypress: controlar relógio sem mascarar espera externa.
- [[cypress-component-testing-boundary]] — Cypress: separar component testing de cobertura end-to-end.
- [[cypress-test-retries-diagnostico]] — Cypress: interpretar test retries como sinal de flakiness.

### Pact
- [[pact-consumer-request-as-sent]] — Pact: capturar a requisição que o cliente realmente envia.
- [[pact-matchers-consumer-relevant]] — Pact: escolher matchers por relevância para o consumidor.
- [[pact-not-functional-provider-test]] — Pact: não usar contrato como teste funcional do provider.
- [[pact-provider-verify-local-instance]] — Pact: verificar contracts contra instância local do provider.
- [[pact-provider-state-setup-per-interaction]] — Pact: preparar provider states determinísticos por interação.
- [[pact-provider-state-false-positive-params]] — Pact: evitar falso positivo por parâmetro de busca ignorado.
- [[pact-stub-below-request-validation]] — Pact: manter stubs abaixo da validação do request.
- [[pact-publish-version-verification-matrix]] — Pact: publicar versões e resultados para compatibilidade.
- [[pact-can-i-deploy-environment-context]] — Pact: testar can-i-deploy contra o ambiente real de destino.
- [[pact-webhook-provider-verification-feedback]] — Pact: tratar webhook como gatilho, não resultado de verificação.

### PostgreSQL
- [[postgresql-read-committed-snapshot-por-statement]] — PostgreSQL: testar snapshots no READ COMMITTED.
- [[postgresql-serializable-retry-serialization-failure]] — PostgreSQL: repetir transação após serialization failure.
- [[postgresql-mvcc-concurrent-read-write]] — PostgreSQL: testar visibilidade MVCC entre conexões.
- [[postgresql-unique-constraint-concorrencia]] — PostgreSQL: validar unicidade sob inserções concorrentes.
- [[postgresql-row-lock-skip-locked-queue]] — PostgreSQL: testar filas com FOR UPDATE SKIP LOCKED.
- [[postgresql-deadlock-sqlstate-retry]] — PostgreSQL: reproduzir deadlock e repetir operação inteira.
- [[postgresql-explain-analyze-execucao-side-effects]] — PostgreSQL: tratar EXPLAIN ANALYZE como execução.
- [[postgresql-sequence-valores-nao-gapless]] — PostgreSQL: não testar sequences como contador sem lacunas.
- [[postgresql-timestamptz-session-timezone]] — PostgreSQL: testar timestamptz com timezone explícito.
- [[postgresql-sqlstate-assertion-errors]] — PostgreSQL: afirmar SQLSTATE em vez de texto de erro.

### GraphQL
- [[graphql-validation-before-resolvers]] — GraphQL: validar operações antes de executar resolvers.
- [[graphql-variable-omitted-null-default]] — GraphQL: distinguir variável omitida de null explícito.
- [[graphql-non-null-null-propagation]] — GraphQL: testar propagação de null em campos non-null.
- [[graphql-partial-data-errors-path]] — GraphQL: aceitar data parcial quando um resolver falha.
- [[graphql-alias-fragment-response-shape]] — GraphQL: testar aliases e fragments pela forma da resposta.
- [[graphql-pagination-cursor-invariants]] — GraphQL: validar invariantes da paginação por cursor.
- [[graphql-dataloader-request-scope]] — GraphQL: testar batching sem compartilhar cache entre usuários.
- [[graphql-authorization-resolver-context]] — GraphQL: verificar autorização no caminho de execução.
- [[graphql-cache-control-private-identities]] — GraphQL: testar cache em respostas autenticadas.
- [[graphql-schema-change-compatibility]] — GraphQL: revisar mudanças de schema com operações consumidoras.

### Apple XCTest
- [[xctest-async-await-test-method]] — XCTest: usar async/await em testes assíncronos Swift.
- [[xctest-expectation-fulfillment-count]] — XCTest: controlar fulfillment e over-fulfillment de expectations.
- [[xctest-waiter-group-timeout]] — XCTest: aguardar grupo de expectativas com resultado explícito.
- [[xctest-ui-accessibility-identifiers]] — XCTest UI tests: selecionar controles por identificadores estáveis.
- [[xctest-app-launch-arguments-environment]] — XCTest UI tests: configurar o app por launch arguments.
- [[xctest-plans-matrix-configurations]] — Xcode test plans: variar configurações de execução intencionalmente.
- [[xctest-signpost-performance-metric]] — XCTest: medir intervalo instrumentado com signpost metric.
- [[xctest-order-independent-state-reset]] — XCTest: não depender da ordem dos métodos de teste.
- [[xctest-locale-device-configuration]] — XCTest: cobrir locale e device sem depender do simulador anterior.
- [[xctest-ui-wait-for-condition-not-sleep]] — XCTest UI tests: aguardar condição da interface, não sleep.

### Kubernetes
- [[kubernetes-job-completion-backoff]] — Kubernetes Job: testar conclusão e retries do controller.
- [[kubernetes-cronjob-no-exactly-once]] — Kubernetes CronJob: testar execução idempotente, não exactly-once.
- [[kubernetes-deployment-rollout-observed-state]] — Kubernetes Deployment: aguardar rollout e validar aplicação.
- [[kubernetes-networkpolicy-plugin-enforcement-test]] — Kubernetes NetworkPolicy: testar enforcement do plugin de rede.
- [[kubernetes-rbac-auth-can-i-identity]] — Kubernetes RBAC: verificar permissão com identidade e escopo.
- [[kubernetes-pdb-voluntary-disruption-test]] — Kubernetes PDB: limitar disrupção voluntária em teste controlado.
- [[kubernetes-hpa-eventual-convergence]] — Kubernetes HPA: testar convergência eventual de réplicas.
- [[kubernetes-configmap-env-vs-volume]] — Kubernetes ConfigMap: testar atualização por env e por volume.
- [[kubernetes-namespace-cleanup-isolation]] — Kubernetes: isolar testes de cluster por namespace descartável.
- [[kubernetes-service-endpoints-readiness]] — Kubernetes Service: testar endpoints prontos sem fixar IP de Pod.

### OpenTelemetry
- [[otel-inmemory-span-exporter-assertions]] — OpenTelemetry: inspecionar spans com exporter em memória.
- [[otel-span-error-status-exception]] — OpenTelemetry: testar exceção e status de span separadamente.
- [[otel-context-propagation-async-boundary]] — OpenTelemetry: preservar contexto em fronteira assíncrona.
- [[otel-resource-scope-instrumentation-identity]] — OpenTelemetry: distinguir resource de instrumentation scope.
- [[otel-inmemory-metrics-reader-aggregation]] — OpenTelemetry: testar agregação de métricas em memória.
- [[otel-histogram-buckets-boundaries]] — OpenTelemetry: testar histograma por limites e distribuição.
- [[otel-log-trace-correlation-context]] — OpenTelemetry: verificar correlação de logs com trace ativo.
- [[otel-cardinality-views-attribute-control]] — OpenTelemetry: testar cardinalidade e views de métricas.
- [[otel-test-provider-exporter-lifecycle]] — OpenTelemetry: isolar exporter e provider entre testes.
- [[otel-semconv-versioned-attributes]] — OpenTelemetry: versionar assertions de semantic conventions.

### pytest
- [[pytest-tmp-path-per-test-files]] — pytest: usar tmp_path para arquivos isolados por teste.
- [[pytest-tmp-path-factory-session-data]] — pytest: reservar tmp_path_factory para artefato caro compartilhado.
- [[pytest-yield-fixture-teardown-order]] — pytest: ordenar teardown de fixtures dependentes.
- [[pytest-fixture-scope-isolation]] — pytest: alinhar escopo de fixture ao ciclo de vida do recurso.
- [[pytest-parametrize-ids-values-reference]] — pytest: nomear parâmetros e proteger dados mutáveis.
- [[pytest-indirect-param-fixture-setup]] — pytest: usar indirect parametrization para setup configurável.
- [[pytest-autouse-fixture-hidden-side-effects]] — pytest: limitar efeitos ocultos de fixtures autouse.
- [[pytest-unittest-fixture-injection-limit]] — pytest: entender limites de fixtures em unittest.TestCase.
- [[pytest-monkeypatch-env-teardown]] — pytest: escopar monkeypatch de ambiente e dependências.
- [[pytest-xfail-strict-expected-failure]] — pytest: ativar strict para xfail não mascarar regressão.

### GitLab CI
- [[gitlab-rules-avoid-duplicate-pipelines]] — GitLab CI: testar rules para evitar pipelines duplicados.
- [[gitlab-merge-request-rules-main-config]] — GitLab CI: garantir que configuração principal habilita MR pipeline.
- [[gitlab-child-pipeline-source-parent-pipeline]] — GitLab CI: reconhecer CI_PIPELINE_SOURCE em child pipeline.
- [[gitlab-trigger-strategy-propagate-result]] — GitLab CI: propagar resultado do downstream ao pipeline pai.
- [[gitlab-needs-artifacts-explicit-dependency]] — GitLab CI: verificar que jobs recebem artifacts necessários.
- [[gitlab-cache-not-artifact]] — GitLab CI: não usar cache como evidência de build.
- [[gitlab-resource-group-serialize-deploy]] — GitLab CI: serializar deploys com resource_group.
- [[gitlab-rules-changes-path-coverage]] — GitLab CI: testar path rules para não pular validação compartilhada.
- [[gitlab-protected-variables-untrusted-pipeline]] — GitLab CI: evitar secrets em pipeline não confiável.
- [[gitlab-parallel-matrix-coverage]] — GitLab CI: validar combinações realmente cobertas por parallel matrix.

### Spring Boot
- [[spring-webmvctest-vs-springboottest]] — Spring Boot: escolher @WebMvcTest ou @SpringBootTest.
- [[spring-mockmvc-vs-random-port]] — Spring Boot: distinguir MockMvc de servidor em porta aleatória.
- [[spring-datajpatest-database-boundary]] — Spring Boot: delimitar @DataJpaTest e o banco usado.
- [[spring-testcontext-cache-dirties-context]] — Spring TestContext: controlar estado em ApplicationContext cacheado.
- [[spring-transactional-test-real-server-threads]] — Spring Boot: não presumir rollback do cliente em RANDOM_PORT.
- [[spring-testresttemplate-status-assertions]] — Spring Boot: afirmar status com TestRestTemplate explicitamente.
- [[spring-restclient-test-slice-mockserver]] — Spring Boot: usar @RestClientTest para cliente HTTP.
- [[spring-active-profiles-test-configuration]] — Spring Boot: declarar perfil de teste sem depender do ambiente local.
- [[spring-webtestclient-mock-vs-server]] — Spring Boot: testar WebTestClient em mock e servidor.
- [[spring-graphql-test-slice-boundary]] — Spring Boot: delimitar @GraphQlTest e integração GraphQL.

## Tranche 10 — frameworks, infraestrutura e ferramentas (notas 350–449)

### Selenium WebDriver: sincronização e interações no navegador
- [[selenium-explicit-wait-condicao-observavel]] — Uma espera explícita consulta uma condição definida até que ela seja verdadeira ou que o timeout configurado expire.
- [[selenium-nao-misturar-esperas-implicit-explicit]] — A espera implícita afeta buscas de elementos, enquanto a explícita aguarda uma condição específica definida pelo teste.
- [[selenium-locators-identidade-estavel]] — Locators traduzem uma propriedade observável do DOM em um alvo para interações WebDriver.
- [[selenium-findelement-find-elements-ausencia]] — findElement retorna um elemento correspondente e sinaliza ausência; findElements retorna uma lista, que pode estar vazia.
- [[selenium-stale-element-relocalizar-apos-render]] — Uma referência WebElement pode ficar obsoleta quando o nó original deixa de pertencer ao DOM ativo.
- [[selenium-frame-trocar-e-restaurar-contexto]] — O driver procura elementos no contexto de navegação atualmente selecionado; conteúdo em iframe requer troca explícita para o frame.
- [[selenium-nova-janela-diferenca-handles]] — WebDriver representa janelas e abas por handles únicos dentro da sessão e não distingue conceitualmente as duas formas.
- [[selenium-alert-wait-accept-dismiss]] — WebDriver expõe alertas, confirmações e prompts nativos por uma API específica após selecionar o alerta ativo.
- [[selenium-actions-sequencia-e-liberacao-input]] — Actions API encadeia comandos de dispositivos de entrada, como teclado, ponteiro e roda, para interações de baixo nível.
- [[selenium-elemento-interativo-validar-estado]] — Comandos de elemento incluem click, send keys, clear e ações apropriadas ao tipo do controle.

### JUnit 6.1.3: parametrização, ciclo de vida e execução
- [[junit-parametrized-test-casos-complementares]] — @ParameterizedTest executa um método repetidamente com argumentos fornecidos por uma fonte declarada.
- [[junit-methodsource-ordem-argumentos]] — MethodSource fornece os argumentos de cada invocação a partir de uma factory method compatível.
- [[junit-dynamic-test-factory-nao-e-caso]] — @TestFactory produz nós DynamicTest ou DynamicContainer em tempo de execução; a factory não é em si um caso de teste.
- [[junit-per-class-estado-compartilhado]] — O lifecycle padrão cria uma instância por método; PER_CLASS reutiliza uma instância para métodos da mesma classe.
- [[junit-parallel-opt-in-modos-e-sincronizacao]] — A execução paralela do Jupiter é opt-in; habilitar o parâmetro global não torna todos os nós concorrentes por padrão.
- [[junit-extension-parameter-resolver-explicito]] — Extensões Jupiter podem resolver parâmetros de métodos e construtores quando um ParameterResolver registrado declara suporte.
- [[junit-tempdir-escopo-e-limpeza]] — A extensão TempDir fornece diretório temporário a um campo ou parâmetro de teste.
- [[junit-tags-filtrar-testes-por-categoria]] — Tags identificam testes e podem ser usadas pelo runner para incluir ou excluir grupos durante uma execução.
- [[junit-condicional-nao-substitui-diagnostico]] — Anotações condicionais e @Disabled controlam se um teste é executado em determinado ambiente ou contexto.
- [[junit-repeated-test-invocacoes-nomeadas]] — @RepeatedTest agenda invocações repetidas de um método e pode expor o número atual e total pelo contexto de repetição.

### Mockito: isolamento de colaboradores e verificação de comportamento
- [[mockito-verificar-contrato-nao-roteiro-interno]] — verify verifica se uma interação esperada ocorreu e pode limitar a quantidade de chamadas.
- [[mockito-stubbing-nao-duplicar-verificacao]] — Stubbing define a resposta de um mock; verificar uma invocação stubada costuma ser redundante quando a saída do sistema já comprova seu uso.
- [[mockito-argumentcaptor-apos-verificacao]] — ArgumentCaptor guarda o argumento passado para uma chamada verificada para permitir assertions específicas sobre seus campos.
- [[mockito-matchers-consistencia-em-todos-argumentos]] — Quando um argumento de uma invocação usa matcher, todos os argumentos dessa mesma invocação precisam ser representados por matchers.
- [[mockito-strict-stubs-detectar-setup-morto]] — STRICT_STUBS ajuda a detectar stubs não utilizados e incompatibilidades entre argumentos configurados e invocações reais.
- [[mockito-lenient-apenas-no-stub-excepcional]] — Lenient permite que um stub escape de verificações estritas como unused stubbing ou argumento potencialmente incorreto.
- [[mockito-spy-metodo-real-e-efeitos-colaterais]] — Um spy delega chamadas não stubadas ao objeto real, diferentemente do mock que usa comportamento simulado.
- [[mockito-stubbing-consecutivo-modelar-retentativas]] — Stubbing consecutivo define respostas diferentes para chamadas subsequentes do mesmo método.
- [[mockito-nao-compartilhar-mock-mutavel-entre-testes]] — reset apaga stubbing e interações de um mock, enquanto clearInvocations limpa interações sem remover o comportamento configurado.
- [[mockito-junit-jupiter-lifecycle-explicito]] — MockitoExtension integra criação de mocks anotados e sessão Mockito ao lifecycle de testes Jupiter.

### Jest 30.5: execução assíncrona, mocks e snapshots
- [[jest-retornar-promise-para-aguardar-assercoes]] — Jest considera uma função assíncrona concluída quando sua Promise retornada resolve ou rejeita.
- [[jest-rejeicoes-async-com-rejects]] — Matchers .rejects permitem verificar o valor ou erro de uma Promise rejeitada e precisam ser retornados ou aguardados.
- [[jest-hooks-escopo-e-ordem]] — beforeAll, beforeEach, afterEach e afterAll organizam setup e cleanup no escopo em que são declarados.
- [[jest-beforeall-nao-compartilha-estado-entre-arquivos]] — beforeAll executa uma vez antes dos testes do escopo atual, não como banco de estado universal entre arquivos.
- [[jest-mock-function-calls-results-context]] — Mock functions registram chamadas, resultados, instâncias e contexto this para assertions sobre colaboração.
- [[jest-clear-reset-restore-mocks-diferencas]] — Clear apaga histórico, reset também substitui implementação configurada, e restore devolve implementação original quando a função é spy.
- [[jest-fake-timers-timers-pendentes-recursivos]] — Fake timers permitem avançar relógio JavaScript sem esperar o tempo real passar.
- [[jest-mock-modulos-esm-commonjs]] — O fluxo de mock de módulo depende do sistema de módulos e da ordem em que imports estáticos são avaliados.
- [[jest-snapshot-revisao-antes-de-atualizar]] — Snapshot armazena uma representação serializada para comparar execuções futuras e detectar mudanças de saída.
- [[jest-coverage-thresholds-nao-medir-qualidade-sozinhos]] — A configuração pode impor thresholds de cobertura globais ou para caminhos específicos e falhar quando o limite não é atingido.

### Vitest: mocks, isolamento e configuração de projetos
- [[vitest-vi-mock-hoisting-importacao]] — vi.mock é elevado pelo transformador do Vitest para executar antes dos imports estáticos do módulo de teste.
- [[vitest-domock-mock-runtime-import]] — vi.doMock registra um mock em runtime e não é içado como vi.mock.
- [[vitest-setupfiles-mocks-modulos-cache]] — Arquivos setupFiles são executados antes dos arquivos de teste e podem carregar módulos antes de um mock local.
- [[vitest-fake-timers-restaurar-relogio]] — vi.useFakeTimers substitui timers do ambiente selecionado até que o teste volte ao relógio real.
- [[vitest-setsystemtime-nao-disparar-timers]] — vi.setSystemTime altera a data percebida pelo código, mas não dispara por si só timers agendados.
- [[vitest-browser-mode-spy-namespace]] — Em Browser Mode, módulos ESM nativos têm namespace de importação que não pode ser substituído como um objeto mutável comum.
- [[vitest-projects-inheritance-opcoes-globais]] — Vitest Projects permite agrupar conjuntos de testes com opções próprias; projetos inline podem herdar configuração conforme extends.
- [[vitest-isolation-parallelism-tradeoff]] — Por padrão, o pool do Vitest isola arquivos de teste; configuração sem isolamento pode compartilhar estado de ambiente e módulos.
- [[vitest-coverage-provider-relatorio-declarado]] — Vitest suporta cobertura via provider nativo v8 ou instrumentação Istanbul, com configuração de reporters.
- [[vitest-snapshot-diff-revisao-intencional]] — Snapshots registram uma saída serializada e falham quando a nova saída difere do baseline salvo.

### Testcontainers para Java: readiness, ciclo de vida e isolamento
- [[testcontainers-startup-check-vs-readiness]] — Startup checks detectam o estado de inicialização do container; wait strategies aguardam uma condição de readiness do serviço.
- [[testcontainers-wait-endpoint-readiness-contract]] — A wait strategy pode observar condições diferentes, incluindo porta, resposta HTTP, healthcheck e logs.
- [[testcontainers-junit-static-vs-instance-containers]] — A extensão Jupiter associa containers estáticos ao ciclo de vida da classe e containers de instância ao lifecycle por teste.
- [[testcontainers-junit5-parallel-extension-limit]] — A integração JUnit Jupiter de Testcontainers documenta que execução paralela não é suportada pela extensão.
- [[testcontainers-manual-lifecycle-cleanup]] — Controle manual permite iniciar recursos fora do lifecycle automático de uma extensão e usá-los em escopo explícito.
- [[testcontainers-jdbc-url-configuracao-reprodutivel]] — O suporte JDBC permite solicitar bancos Testcontainers por URL jdbc:tc e associar o driver e módulo apropriados.
- [[testcontainers-reuse-opt-in-estado-persistente]] — Reusable Containers requer opt-in e configuração idêntica para que uma execução reutilize o recurso anterior.
- [[testcontainers-compose-espera-servico-especifico]] — A integração com Compose permite identificar serviços expostos e associar uma wait strategy ao serviço relevante.
- [[testcontainers-pinar-imagem-para-reprodutibilidade]] — Uma tag específica reduz mudanças inesperadas da imagem, enquanto um digest pode identificar exatamente o artefato resolvido.
- [[testcontainers-startup-parallel-independencia-recursos]] — Opções avançadas permitem reduzir tempo de inicialização de containers quando o setup possui serviços independentes.

### Grafana k6: modelagem de carga, métricas e thresholds
- [[k6-checks-precisam-threshold-para-falhar]] — Checks registram se uma condição observável passou, mas checks falhados não abortam nem reprovam sozinhos o teste.
- [[k6-thresholds-criterios-operacionais-pass-fail]] — Thresholds expressam condições de aprovação sobre métricas e podem afetar o resultado final de uma execução.
- [[k6-scenarios-executors-workload-nomeado]] — Scenario descreve como executar funções de teste e escolhe executor, duração, usuários ou taxa de iteração.
- [[k6-open-arrival-closed-vus]] — Executors baseados em VUs mantêm usuários virtuais que iniciam nova iteração após a anterior; arrival-rate agenda iterações por taxa.
- [[k6-dropped-iterations-capacidade-vus]] — Arrival-rate executors podem deixar de iniciar iterações quando não há VUs disponíveis ou o tempo máximo termina.
- [[k6-setup-teardown-dados-compartilhados]] — setup prepara dados antes dos cenários; seus dados JSON são copiados para cada VU e para teardown, não compartilhados como um objeto JavaScript mutável.
- [[k6-tags-segmentar-metricas-sem-alta-cardinalidade]] — Tags categorizam requests, checks, thresholds e métricas customizadas para filtragem e comparação.
- [[k6-threshold-por-tag-e-escopo-de-metrica]] — Threshold pode selecionar subconjuntos de métricas filtrando tags associadas aos samples.
- [[k6-sleep-pacing-representar-think-time]] — sleep(t) suspende o VU pelo número de segundos informado e pode representar think time quando a pausa fizer parte do workload.
- [[k6-browser-protocolo-e-experiencia-complementares]] — O módulo browser do k6 combina automação de navegador com métricas de desempenho frontend para jornadas sintéticas.

### OWASP ZAP: varredura passiva, ativa e automação segura
- [[zap-baseline-scan-passivo-sem-ataque]] — O Docker Baseline Scan realiza spidering e passive scanning, sem executar active attacks contra o alvo.
- [[zap-api-scan-definicao-e-active-scan]] — API Scan importa definições como OpenAPI, SOAP ou GraphQL e aplica varredura adaptada ao formato.
- [[zap-active-scan-autorizacao-e-ambiente]] — Active Scan envia requisições de ataque para identificar vulnerabilidades e pode alterar ou sobrecarregar o sistema alvo.
- [[zap-warnings-exitstatus-politica-ci]] — Automation Framework oferece job exitStatus para derivar o status da execução dos resultados configurados.
- [[zap-automation-framework-plano-yaml]] — Automation Framework executa jobs sequenciais a partir de um plano YAML com ambiente e configuração definidos.
- [[zap-passive-scan-wait-antes-do-relatorio]] — O job passiveScan-wait aguarda que o scanner passivo termine de processar a fila atual.
- [[zap-autenticacao-verificar-sessao-do-scan]] — ZAP suporta métodos de autenticação e verificações de sessão configurados no ambiente e no contexto.
- [[zap-alert-filter-excecao-com-justificativa]] — Alert Filters podem sobrescrever o risco de alertas de scans ativos e passivos; há regras globais e associadas a contexto.
- [[zap-relatorio-artefato-e-evidencia]] — O add-on de Report Generation produz relatórios em formatos configuráveis e tem suporte ao Automation Framework.
- [[zap-separar-passive-active-pipeline]] — Baseline passivo e varredura ativa têm efeitos e evidências diferentes e podem exigir agendas de pipeline diferentes.

### Schemathesis: geração baseada em schema e fluxos de API
- [[schemathesis-schema-inputs-e-checks]] — Schemathesis lê schema OpenAPI ou GraphQL para construir entradas e exercitar operações documentadas.
- [[schemathesis-fases-coverage-fuzzing-stateful]] — Data generation inclui estratégias e fases diferentes, como exemplos, coverage, fuzzing e execução stateful.
- [[schemathesis-valid-invalid-modes-contrato]] — Modos de geração podem focar entradas conformes ou violadoras do schema para testar aceitação e rejeição.
- [[schemathesis-shrinking-reproducao-falha]] — Shrinking busca reduzir uma entrada que reproduz uma falha para um caso menor e mais diagnóstico.
- [[schemathesis-stateful-links-sequencia-api]] — OpenAPI Links permite mapear explicitamente dados de uma resposta para parâmetros de outra operação e modelar relações stateful específicas.
- [[schemathesis-stateful-sem-link-nao-presumir]] — Schemathesis pode inferir conexões stateful por análise do schema OpenAPI, aprender relações de cabeçalhos Location no CLI e usar Links explícitos quando necessário.
- [[schemathesis-checks-server-error-schema-status]] — Checks centrais podem detectar erros do servidor, status não documentados e respostas incompatíveis com o schema.
- [[schemathesis-autenticacao-precedencia-e-sanitizacao]] — Schemathesis aceita autenticação por CLI, configuração ou mecanismo associado ao schema, com precedência definida pela ferramenta.
- [[schemathesis-pytest-parametrize-call-and-validate]] — A integração pytest parametriza testes pelas operações e oferece Case para executar e validar respostas.
- [[schemathesis-orcamento-exemplos-rate-limit]] — `generation.max-examples` limita casos da fase fuzzing por operação e sequências stateful; examples e coverage adicionam seus próprios casos.

### StrykerJS: mutation testing e interpretação de resultados
- [[stryker-dry-run-suite-original-passa]] — Stryker executa um dry run sem mutações antes de iniciar a avaliação de mutants.
- [[stryker-killed-survived-no-coverage]] — Killed indica que um teste falhou com o mutant ativo; survived e No coverage são undetected, enquanto Ignored é excluído intencionalmente da avaliação.
- [[stryker-threshold-break-falha-pipeline]] — Thresholds high e low classificam a pontuação, enquanto break pode fazer a execução terminar com erro abaixo do limite.
- [[stryker-coverage-analysis-custos-e-classificacao]] — Coverage analysis pode selecionar quais testes executar para cada mutant e distinguir categorias conforme dados do runner.
- [[stryker-incremental-resultados-cache-validade]] — Incremental mode reutiliza resultados quando arquivos mutados e testes não mudaram segundo o diff que o runner suporta.
- [[stryker-mutate-apenas-codigo-de-producao]] — A opção mutate seleciona arquivos e padrões sujeitos a alterações artificiais.
- [[stryker-ignore-mutant-justificado-e-visivel]] — Stryker permite excluir mutators, usar comentários disable ou plugins ignore para padrões específicos.
- [[stryker-static-mutants-pertest-requirement]] — StrykerJS exige coverageAnalysis perTest para ignoreStatic; mutants estáticos ignorados aparecem como Ignored e não contam no mutation score.
- [[stryker-timeout-investigar-runner-e-mutante]] — A configuração oferece limites temporais para processos de teste e execução de mutants.
- [[stryker-equivalent-mutant-score-interpretacao]] — Mutation score resume resultados de mutants no escopo selecionado, mas não classifica automaticamente equivalência semântica.

## Tranche 11 — frameworks, protocolos, carga e automação móvel (notas 450–549)

### REST Assured: contratos HTTP testáveis em Java
- [[restassured-given-when-then-fronteira]] — O padrão given/when/then organiza a especificação da requisição, a execução do HTTP e as expectativas sobre a resposta.
- [[restassured-request-specification-reuso-isolado]] — RequestSpecification agrupa dados de request que podem ser compostos e reaproveitados em várias chamadas.
- [[restassured-response-specification-contrato-comum]] — Uma response specification permite reutilizar assertions comuns para respostas de vários testes.
- [[restassured-path-query-parameters-distintos]] — Path parameters substituem segmentos nomeados do caminho; query parameters são enviados na parte de consulta da URL.
- [[restassured-object-mapping-dependencias-explícitas]] — REST Assured pode serializar objetos Java para JSON ou XML e desserializar respostas quando os mapeadores compatíveis estão disponíveis no classpath.
- [[restassured-jsonpath-extrair-depois-de-validar]] — JsonPath permite selecionar valores do corpo JSON da resposta para assertions ou etapas posteriores do teste.
- [[restassured-json-schema-validacao-opcional]] — REST Assured oferece matcher para validar um corpo JSON contra um schema, disponível pela integração de validação correspondente.
- [[restassured-filtros-logging-nao-e-wire-capture]] — Filters podem observar ou alterar request antes do envio e response antes das expectations; filtros também podem implementar logging ou autenticação.
- [[restassured-auth-por-caso-sem-credencial-em-log]] — REST Assured suporta esquemas de autenticação e configuração de credenciais por request.
- [[restassured-configuracao-global-reset-e-paralelismo]] — REST Assured expõe defaults estáticos como base URI, filtros e specifications que influenciam requests posteriores.

### WireMock: stubs HTTP, estados e diagnóstico de interações
- [[wiremock-mapping-request-response-contrato]] — Um stub WireMock associa condições de request a uma response configurada por código ou arquivo JSON.
- [[wiremock-urlpath-query-param-matching]] — WireMock permite comparar URL completa ou só o path e declarar query parameters separadamente.
- [[wiremock-json-body-matcher-estrutura]] — WireMock fornece matchers de corpo JSON que comparam conteúdo estruturado, além de comparação literal ou JSONPath.
- [[wiremock-priority-sobreposicao-stubs]] — Se múltiplos stubs combinam com uma request, a prioridade controla qual resposta é selecionada; números menores indicam prioridade maior.
- [[wiremock-scenario-maquina-de-estados]] — Um cenário WireMock representa uma máquina de estados simples; mappings podem exigir estado e mudar o estado após uma request.
- [[wiremock-verificacao-de-request-journal]] — O request journal mantém requests recebidas em memória para verificação e consulta após as chamadas do sistema sob teste.
- [[wiremock-unmatched-requests-near-miss]] — Requests sem mapping normalmente recebem 404 e podem ser consultadas como unmatched; near misses apontam mappings parecidos.
- [[wiremock-faults-para-resiliencia]] — WireMock pode simular falhas de transporte para observar como o cliente trata interrupções e respostas incompletas.
- [[wiremock-junit-extension-reset-por-teste]] — A extensão WireMock para JUnit Jupiter inicia e encerra servidor conforme lifecycle e, por padrão, reseta mappings e requests entre métodos.
- [[wiremock-response-template-dados-da-request]] — Response templating pode preencher partes da resposta com valores do contexto da request em vez de manter uma fixture fixa.

### Robot Framework 7.5: keywords, fixtures e dados de teste
- [[robot-test-case-keywords-observáveis]] — Um caso Robot Framework contém chamadas a keywords descritas nas seções de teste e executadas pelas bibliotecas importadas.
- [[robot-setup-teardown-escopo]] — Setups e teardowns podem ser definidos no nível de caso ou suite e executam keywords antes/depois da unidade configurada.
- [[robot-tags-selecao-sem-substituir-assertions]] — Tags podem classificar casos e orientar a seleção de testes durante a execução.
- [[robot-template-data-driven]] — Um test template transforma as linhas de argumentos de um caso em chamadas repetidas à keyword-template escolhida.
- [[robot-variaveis-escopo-prioridade]] — Robot Framework oferece variáveis de diferentes origens e escopos, e sua resolução depende da origem e do momento da definição.
- [[robot-resource-vs-library-import]] — Resource files compartilham user keywords e dados Robot; libraries fornecem keywords implementadas em Python ou outra integração suportada.
- [[robot-keyword-argumentos-e-conversao]] — User keywords podem receber argumentos nomeados ou posicionais e podem expor valores de retorno a outras keywords.
- [[robot-ignore-error-nao-esconder-falha]] — Run Keyword And Ignore Error captura falha de keyword e devolve status e mensagem, permitindo tratamento deliberado no fluxo.
- [[robot-wait-until-keyword-succeeds-idempotência]] — Wait Until Keyword Succeeds repete uma keyword em intervalo configurado até passar ou esgotar limite.
- [[robot-output-report-sensitive-data]] — Uma execução Robot gera output.xml e relatórios/logs configuráveis que ajudam a diagnosticar os casos executados.

### Cucumber e Gherkin: especificações executáveis sem ambiguidade
- [[cucumber-feature-scenario-executable-spec]] — Uma Feature agrupa cenários relacionados e cada Example ou Scenario descreve contexto, evento e resultado esperado em steps.
- [[cucumber-keywords-nao-fazem-parte-do-matching]] — A palavra Given, When ou Then dá semântica ao texto, mas não é usada por Cucumber para distinguir step definitions durante matching.
- [[cucumber-expressions-parametros-tipados]] — Step definitions podem usar Cucumber Expressions ou regular expressions e receber valores capturados como argumentos.
- [[cucumber-step-definitions-ambiguos-unicos]] — Cucumber precisa de uma definição única que corresponda ao texto de cada step; mais de uma correspondência impede execução inequívoca.
- [[cucumber-scenario-outline-examples-linhas]] — Scenario Outline é um template; suas steps recebem valores de placeholders e o outline executa uma vez para cada linha em Examples.
- [[cucumber-data-tables-argumento-final]] — Uma DataTable é passada como argumento multilinha final à step definition e pode ser convertida conforme sua forma e tipo.
- [[cucumber-doc-string-corpo-multilinha]] — Gherkin permite Doc Strings como argumento de step para passar texto longo, como JSON, GraphQL ou uma mensagem.
- [[cucumber-background-precondicao-compartilhada]] — Background define steps comuns executados antes dos cenários aplicáveis dentro da Feature ou Rule.
- [[cucumber-hooks-condicionais-com-tags]] — Hooks podem ser associados a expressões de tags para executar preparação ou limpeza em cenários selecionados.
- [[cucumber-tags-selecao-e-inclusao]] — Tags podem organizar features e cenários e selecionar subconjuntos de execução; expressões também podem restringir hooks.

### NUnit: parametrização, lifecycle e execução paralela
- [[nunit-test-async-await-task]] — NUnit aceita test methods async que retornam Task ou Task<T> e registra o resultado após a conclusão.
- [[nunit-testcase-cada-argumento-caso]] — TestCase fornece argumentos inline para um método parametrizado e permite que cada combinação seja descoberta como test case.
- [[nunit-testcasesource-fonte-enumeravel]] — TestCaseSource identifica campo, propriedade ou método que fornece argumentos para casos parametrizados.
- [[nunit-setup-teardown-por-caso]] — SetUp é chamado antes de cada test method e TearDown logo depois de cada test case na fixture.
- [[nunit-onetimesetup-hierarquia-fixture]] — OneTimeSetUp executa uma vez antes dos testes filhos da fixture; classes base e derivadas seguem ordem de herança documentada.
- [[nunit-setupfixture-escopo-namespace]] — SetUpFixture oferece setup e teardown únicos para fixtures pertencentes a namespace e subnamespaces na assembly.
- [[nunit-fixturelifecycle-instance-per-case]] — FixtureLifeCycle pode usar instância única por fixture ou instância nova por test case.
- [[nunit-parallelizable-nao-e-limite-de-workers]] — Parallelizable marca testes ou descendentes elegíveis para concorrência; LevelOfParallelism define o teto de workers da assembly.
- [[nunit-order-local-nao-sincroniza-conclusao]] — Order organiza quando testes ou fixtures começam dentro da suite que os contém; não ordena globalmente nem aguarda término anterior.
- [[nunit-testcontext-diagnostico-por-escopo]] — TestContext fornece dados do execution context e distingue contexto de caso em método/setup/teardown de contexto de fixture nos métodos one-time.

### xUnit.net v3: dados, fixtures e paralelismo
- [[xunit-fact-vs-theory-escopo]] — Fact representa um caso individual; Theory associa a um método conjuntos de dados que produzem invocações parametrizadas.
- [[xunit-inline-data-casos-visíveis]] — InlineData fornece argumentos constantes para Theory e cada linha representa um caso executável.
- [[xunit-memberdata-classdata-provedor-tipado]] — Theories podem obter dados de membros ou classes provedoras, separando matriz de argumentos da lógica do teste.
- [[xunit-constructor-dispose-instancia-por-teste]] — xUnit cria instância nova da classe de teste para cada test que executa; constructor e Dispose oferecem preparação e limpeza por instância.
- [[xunit-class-fixture-compartilhar-recurso]] — IClassFixture compartilha uma instância de fixture entre os testes de uma classe e a descarta depois da classe.
- [[xunit-collection-fixture-serializar-recurso]] — Collection fixtures compartilham fixture entre classes associadas à mesma collection; classes na collection deixam de executar paralelamente entre si.
- [[xunit-async-lifetime-teardown]] — xUnit oferece interfaces de lifecycle assíncrono para inicialização e limpeza; suportes de DisposeAsync diferem entre v2 e v3.
- [[xunit-paralelismo-por-collection-isolar]] — No modo collections, testes de uma collection não rodam em paralelo entre si, mas collections distintas podem concorrer.
- [[xunit-outputhelper-saida-associada]] — ITestOutputHelper fornece saída associada ao test case, enquanto Console e Trace são recursos compartilhados do processo.
- [[xunit-assert-throws-tipo-exato]] — Assert.Throws e variantes assíncronas capturam exceção da operação e permitem verificar tipo e conteúdo da falha.

### Locust: cenários de usuário e geração de carga Python
- [[locust-httpuser-nao-e-browser]] — HttpUser oferece client HTTP e mantém cookies, mas não renderiza HTML nem carrega automaticamente recursos da página como browser.
- [[locust-task-weights-probabilidade]] — Decorador @task com peso faz Locust escolher tarefas com frequência relativa entre as opções disponíveis do usuário.
- [[locust-wait-time-pos-task-nao-rps]] — wait_time é aplicado após a execução de uma tarefa; ausência de wait_time inicia a próxima task assim que a atual termina.
- [[locust-on-start-stop-lifecycle]] — on_start e on_stop são callbacks por instância de User que permitem iniciar e encerrar contexto do usuário simulado.
- [[locust-request-name-cardinalidade]] — O parâmetro name do client pode agrupar requests com paths ou query values diferentes sob um nome de estatística comum.
- [[locust-catch-response-validacao-manual]] — Cliente HTTP de Locust permite inspecionar resposta no bloco catch_response e decidir manualmente se a chamada conta como sucesso ou falha.
- [[locust-taskset-sequencia-de-tarefas]] — TaskSet organiza conjunto de tarefas e pode delegar para subtasksets; SequentialTaskSet expressa sequência declarada quando a jornada requer ordem.
- [[locust-loadtestshape-tick]] — LoadTestShape permite controlar usuários e spawn rate através de tick, que retorna a população desejada e pode terminar com None.
- [[locust-distributed-master-worker]] — Em execução distribuída, master coordena interface e spawn/stop; workers executam Users e enviam estatísticas ao master.
- [[locust-fast-httpuser-gerador-versus-alvo]] — FastHttpUser pode reduzir overhead de cliente HTTP quando Locust precisa gerar uma taxa alta de requests.

### Apache JMeter: planos de teste e carga reproduzível
- [[jmeter-threadgroup-threads-independentes]] — Cada thread de um Thread Group executa o plano de teste de forma independente e pode representar uma conexão/usuário concorrente.
- [[jmeter-timer-before-samplers-scope]] — Timer é processado antes de cada sampler dentro do escopo hierárquico, e múltiplos timers podem acumular atraso.
- [[jmeter-assertion-aplica-por-escopo]] — Assertions são executadas após samplers no escopo onde aparecem e verificam campos de request/response configurados.
- [[jmeter-csv-dataset-dados-por-thread]] — CSV Data Set Config lê registros em variáveis e normalmente fornece linhas diferentes às threads do plano.
- [[jmeter-thread-variables-properties-compartilhamento]] — Variáveis de JMeter têm escopo de thread, enquanto properties são compartilhadas entre threads do processo.
- [[jmeter-cli-para-carga-gui-para-debug]] — Manual recomenda GUI para criar/debuggar plano e CLI mode para load test com menor overhead de interface.
- [[jmeter-execution-order-processors]] — JMeter processa elementos da árvore em ordem definida, com configuration elements e preprocessors antes do sampler e postprocessors/assertions depois.
- [[jmeter-listeners-impacto-gerador]] — Listeners exibem, salvam ou processam resultados e podem consumir recursos do gerador conforme volume e formato.
- [[jmeter-transaction-controller-unidades-medicao]] — Transaction Controller agrupa samplers em transação e pode produzir sample agregado conforme modo configurado.
- [[jmeter-testplan-versioned-results]] — Plano JMX e properties determinam execução; registrar apenas arquivo de resultado não permite reproduzir configuração de carga.

### Gatling: cenários, sessão e critérios de performance
- [[gatling-scenario-exec-sequencia]] — Um ScenarioBuilder encadeia ações com exec; requests e funções executadas no cenário seguem a sequência declarada.
- [[gatling-session-estado-por-virtual-user]] — Session representa o estado de um virtual user e carrega atributos ao longo das ações do scenario.
- [[gatling-feeder-dados-variados-cache]] — Feeder fornece records aos virtual users por meio de feed e os atributos passam para Session.
- [[gatling-check-saveas-apos-sucesso]] — Checks validam request/response e podem extrair um valor para Session; saveAs só é efetivo quando check passa.
- [[gatling-assertions-criterios-de-simulacao]] — Assertions na Simulation definem critérios sobre estatísticas globais ou escopos como requests/grupos.
- [[gatling-open-closed-injection-model]] — Perfis open injetam usuários por taxa de chegada; closed model define concorrência de usuários cuja duração influencia novas iterações.
- [[gatling-groups-agregacao-por-jornada]] — Groups agrupam ações do usuário e permitem observar estatísticas relativas a uma parte nomeada do scenario.
- [[gatling-pauses-e-pacing]] — Pause modela intervalo entre ações do scenario; injection controla chegada/concorrência inicial de virtual users.
- [[gatling-protocol-config-comum]] — Protocol configuration reúne base URL, headers e opções compartilhadas que podem ser associadas a um ou mais cenários.
- [[gatling-session-debug-fora-da-carga]] — Session pode ser inspecionada durante desenvolvimento para diagnosticar feeders, expressões e check failures.

### Appium: sessões e automação móvel multiplataforma
- [[appium-driver-instalacao-modular]] — Appium separa o servidor central de drivers que implementam automação por plataforma e precisam ser instalados para criar sessões.
- [[appium-capabilities-prefix-vendor]] — Capabilities são parâmetros key-value de criação de sessão e não podem ser alteradas durante seu lifecycle; capabilities não padrão usam prefixo vendor como appium:.
- [[appium-automationname-seleciona-driver]] — appium:automationName indica qual driver deve executar comandos da sessão.
- [[appium-context-native-webview]] — Contexts representam modos de automação que o driver implementa; API permite listar, ler contexto atual e trocar para outro nome disponível.
- [[appium-session-finally-delete]] — Quickstart abre session remota e chama deleteSession ao concluir interação; lifecycle da sessão é responsabilidade do cliente de teste.
- [[appium-w3c-actions-vs-comandos-driver]] — Appium oferece comandos W3C e extensões específicas do driver; migrações podem remover endpoints touch legados e apontar alternativas.
- [[appium-parallel-device-identidade-ports]] — Capabilities como udid identificam dispositivo alvo; drivers também podem requerer portas e recursos distintos para sessões simultâneas.
- [[appium-uiautomator2-android-boundary]] — UiAutomator2 é driver oficial para Android e documenta capabilities, comandos e requisitos que não são universais a todo Appium.
- [[appium-xcuitest-ios-boundary]] — XCUITest é driver oficial para apps iOS e seus requisitos dependem do host, toolchain Apple e configuração da sessão.
- [[appium-locators-acessibilidade-contrato]] — Drivers expõem estratégias de locator dependentes da plataforma, incluindo identificadores de acessibilidade ou recursos nativos.

## Tranche 12 — frameworks, propriedades e ferramentas de teste (IDs 550–649; revisão factual por IA registrada)

### Playwright Test — projetos, servidores e artefatos de execução

550. [[playwright-projects-browser-matrix]] — Um projeto nomeado combina os testes com opções de execução, como browser, dispositivo ou ambiente.
551. [[playwright-project-dependencies-setup]] — Uma dependência de projeto permite executar testes de preparação antes dos projetos consumidores e declarar teardown associado.
552. [[playwright-webserver-readiness-reuse]] — A opção `webServer` inicia um processo de aplicação e aguarda a URL configurada responder antes de liberar os testes.
553. [[playwright-sharding-ci-particionamento]] — O parâmetro `--shard=x/y` seleciona uma parte da suíte, permitindo distribuir a execução entre jobs independentes.
554. [[playwright-visual-snapshots-baseline]] — `toHaveScreenshot()` compara uma captura atual com uma imagem de referência gerada e versionada para aquele teste.
555. [[playwright-page-object-contract]] — Um Page Object encapsula seletores e ações recorrentes de uma parte da aplicação, expondo aos testes uma interface de maior nível.
556. [[playwright-download-save-context]] — O evento de download fornece um objeto temporário cujo arquivo é removido quando o browser context que o criou é encerrado.
557. [[playwright-apirequest-cookie-context]] — O `APIRequestContext` ligado ao browser context usa o mesmo jar de cookies; uma instância criada isoladamente mantém armazenamento próprio.
558. [[playwright-test-step-relatorio]] — `test.step()` agrupa uma parte assíncrona do teste sob um nome que aparece como etapa da execução.
559. [[playwright-reporter-saida-por-ambiente]] — O runner inclui reporters com níveis de detalhe distintos e permite configurar mais de um para a mesma execução.
### Hypothesis — construção de estratégias, replay e configuração

560. [[hypothesis-strategy-combinators]] — Combinadores transformam ou encadeiam estratégias sem precisar reescrever o gerador e sua lógica de redução.
561. [[hyp-composite-dependent-strategies]] — `@composite` permite combinar draws de estratégias em um gerador reutilizável cuja saída depende dos valores já sorteados.
562. [[hyp-data-draw-dinamico]] — `st.data()` fornece ao teste uma interface para sortear valores adicionais durante a execução a partir de estratégias escolhidas pelo próprio caso gerado.
563. [[hyp-builds-from-type-infer]] — `builds()` pode criar instâncias de uma classe chamando seu construtor e, quando autorizado, inferindo estratégias a partir de anotações de tipo.
564. [[hyp-valid-collections-cardinality]] — Estratégias de listas, conjuntos e dicionários permitem declarar cardinalidade e tipo dos elementos diretamente no domínio gerado.
565. [[hyp-floats-dominio-na-infinito]] — Estratégias de ponto flutuante podem incluir valores especiais como NaN e infinito, além de valores finitos próximos aos limites declarados.
566. [[hyp-example-regressao-explicito]] — `@example` acrescenta uma entrada escolhida manualmente à execução de um teste baseado em propriedades.
567. [[hyp-example-database-replay]] — O banco de exemplos guarda entradas que Hypothesis encontrou e pode reutilizá-las em execuções posteriores da mesma configuração.
568. [[hyp-settings-profiles-healthchecks]] — Perfis de `settings` agrupam escolhas como orçamento de exemplos e comportamento de deadlines para ambientes com necessidades distintas.
569. [[hyp-deadline-tempo-execucao]] — O `deadline` limita quanto cada exemplo gerado pode gastar em execução, separando lentidão localizada de um teste que simplesmente consome o orçamento total da suíte.
### TestNG — dados, configuração, dependências e execução

570. [[testng-dataprovider-casos]] — `@DataProvider` associa conjuntos de argumentos a uma função `@Test`, e cada linha retornada precisa ser atribuível aos parâmetros daquele método.
571. [[testng-parameters-escopo-xml]] — `@Parameters` injeta valores declarados no `testng.xml` em métodos de teste ou de configuração que declaram os nomes correspondentes.
572. [[testng-dependencies-hard-soft]] — `dependsOnMethods` ou `dependsOnGroups` expressam pré-requisitos de execução e podem fazer o framework pular um consumidor quando uma dependência falha.
573. [[testng-groups-selecao]] — Groups etiquetam métodos ou classes e podem ser incluídos ou excluídos em configuração XML ou na linha de comando.
574. [[testng-lifecycle-heranca-hooks]] — Os métodos `@Before...` e `@After...` descrevem fases diferentes do ciclo de vida e são herdados por classes de teste.
575. [[testng-dataprovider-parallel]] — Um `DataProvider` pode pedir ao TestNG que execute em paralelo os testes gerados por suas linhas de dados.
576. [[testng-suite-parallel-threadcount]] — A suite TestNG configura se métodos, classes, testes ou instâncias são executados em paralelo e quantas threads podem ser usadas.
577. [[testng-factory-instancias]] — `@Factory` retorna objetos que o TestNG trata como instâncias de classes de teste, enquanto `@DataProvider` fornece argumentos para métodos.
578. [[testng-listener-eventos-relatorio]] — Listeners recebem eventos ou oportunidades de extensão durante a execução e podem ser registrados por anotação ou configuração da suite.
579. [[testng-invocationcount-timeout]] — `invocationCount` repete um método de teste e `invocationTimeOut` limita o tempo acumulado dessas invocações quando a contagem está definida.
### Go testing — subtestes, concorrência, fuzzing e benchmarks

580. [[go-subtests-run-filter]] — `t.Run` cria um subteste nomeado associado ao teste pai e possibilita executar subconjuntos por expressão de seleção.
581. [[go-t-cleanup-subtest-scope]] — `T.Cleanup` registra uma função que roda quando o teste e seus subtestes concluírem, respeitando ordem inversa de registro.
582. [[go-testing-helper-error-location]] — `T.Helper` marca uma função auxiliar de teste para que diagnósticos de `Error` ou `Fatal` apontem ao chamador relevante.
583. [[go-parallel-subtests-barreira]] — Um subteste que chama `t.Parallel` pausa até a função do teste pai retornar, e o pai aguarda a conclusão dos filhos paralelos.
584. [[go-fuzz-corpus-regressao]] — Um fuzz test pode combinar sementes declaradas no código com arquivos de corpus, e entradas que revelam falhas podem ser salvas para reprodução.
585. [[go-race-dinamico-limites]] — O detector de corridas instrumenta o programa e reporta acessos concorrentes incompatíveis que aconteceram durante a execução observada.
586. [[go-testing-synctest-tempo-virtual]] — `testing/synctest` executa código concorrente em uma bolha isolada com tempo virtual para testes que dependem de timers e goroutines.
587. [[go-testmain-recursos-pacote]] — `TestMain(m *testing.M)` dá ao pacote um ponto único para preparar recursos antes de rodar seus testes e limpar depois.
588. [[go-tdir-cleanup-descendants]] — `T.TempDir` cria um diretório temporário exclusivo para o teste e o remove quando o teste e seus descendentes terminam.
589. [[go-b-loop-benchmark-comparacao]] — `B.Loop` fornece uma forma atual de escrever o corpo repetido de um benchmark sem controlar manualmente `b.N`.
### PIT — mutation testing para Java

590. [[pit-mutacao-bytecode-mutantes]] — PIT aplica mutadores ao bytecode compilado para criar versões pequenas do programa que representam falhas hipotéticas.
591. [[pit-cobertura-selecao-testes]] — Antes de executar casos contra mutantes, PIT mede cobertura de linha e tempos para selecionar testes que alcançam a área modificada.
592. [[pit-status-killed-survived]] — PIT classifica resultados como `Killed`, `Survived`, `No coverage`, `Non viable` e `Timed Out`, entre outros estados documentados.
593. [[pit-mutator-groups-esforco]] — PIT oferece grupos de mutadores com alcances diferentes, incluindo `DEFAULTS`, `STRONGER` e `ALL`.
594. [[pit-targetclasses-targettests]] — `targetClasses` e `targetTests` definem, respectivamente, quais classes podem receber mutações e quais testes podem participar da análise.
595. [[pit-timeouts-mutantes-hang]] — PIT usa limite temporal para evitar que um mutante que provoque loop ou execução longa bloqueie indefinidamente a análise.
596. [[pit-incremental-history-assumptions]] — A análise incremental conserva resultados anteriores e evita recomputar mutações que PIT considera inferíveis a partir de código e testes não alterados.
597. [[pit-maven-dry-run-setup]] — O modo dry run, documentado desde PIT 1.17.3, reúne cobertura e gera mutantes sem executar a suíte contra cada mutação.
598. [[pit-maven-goal-relatorio]] — O plugin Maven expõe o goal `mutationCoverage`, que compila e executa a análise conforme os filtros definidos no projeto.
599. [[pit-mutation-score-interpretacao]] — Mutation score resume proporções de estados dos mutantes, mas não descreve quais requisitos foram testados nem o custo de interpretar sobreviventes.
### PHPUnit — descoberta, dados, fixtures e execução

600. [[phpunit-discovery-metodos-atributos]] — PHPUnit descobre métodos públicos com prefixo `test` ou métodos marcados com o atributo `#[Test]`.
601. [[phpunit-dataprovider-contrato]] — Um data provider associa conjuntos de argumentos a um método de teste e faz cada conjunto aparecer como uma execução identificável.
602. [[phpunit-testwith-inline-cases]] — O atributo `#[TestWith]` permite associar dados inline ao teste, enquanto `#[DataProvider]` mantém datasets maiores em um método nomeado.
603. [[phpunit-depends-retorno]] — `#[Depends]` declara que um teste consome o valor retornado por outro teste, mas não define sozinho a ordem de execução dos métodos.
604. [[phpunit-fixtures-per-test]] — O PHPUnit cria uma instância da classe de teste por método; `setUp()` e `tearDown()` rodam em cada caso, enquanto `setUpBeforeClass()` e `tearDownAfterClass()` cobrem o ciclo da classe.
605. [[phpunit-config-precedencia]] — A configuração efetiva é construída dos defaults internos, depois do XML e por fim das opções de CLI.
606. [[phpunit-selection-filter-group]] — O runner oferece opções para selecionar suite, grupo ou padrão de nome sem precisar editar a descoberta da classe.
607. [[phpunit-random-seed-repro]] — A opção `--order-by random` executa testes em ordem pseudoaleatória e aceita uma seed para repetir a mesma sequência.
608. [[phpunit-risky-output-assertions]] — PHPUnit pode classificar como arriscados testes sem assertions úteis ou que produzem saída, conforme verificações habilitadas.
609. [[phpunit-size-time-budget]] — Atributos Small, Medium e Large classificam testes por custo e permitem aplicar limites temporais correspondentes na configuração.
### RSpec — exemplos compartilhados, hooks, matchers e seleção

610. [[rspec-shared-examples-contrato]] — Shared examples guardam comportamentos que podem ser executados no contexto de diferentes example groups.
611. [[rspec-include-vs-it-behaves-like]] — `include_examples` inclui o conteúdo no contexto corrente, enquanto `it_behaves_like` cria um grupo aninhado para o comportamento compartilhado.
612. [[rspec-around-hook-envelope]] — Um hook `around(:example)` recebe o objeto de exemplo e envolve a execução que ocorre em `example.run`.
613. [[rspec-before-after-scope]] — Hooks `before` e `after` podem ser definidos para exemplos ou grupos e participam de uma ordem que depende do escopo.
614. [[rspec-composable-matchers-estruturas]] — Matchers compostos permitem descrever partes importantes de uma estrutura aninhada sem exigir que todo valor coincida literalmente.
615. [[rspec-verifying-doubles-interface]] — Verifying doubles checam se métodos configurados existem na classe ou objeto representado, reduzindo divergências entre mock e implementação.
616. [[rspec-message-argument-constraints]] — `with` limita quais argumentos satisfazem uma expectativa ou resposta configurada para uma mensagem recebida por double.
617. [[rspec-metadata-tag-selection]] — Metadata é associada a example groups e exemplos e pode selecionar quais casos entram numa execução da CLI.
618. [[rspec-random-order-seed]] — RSpec pode embaralhar grupos e exemplos usando uma seed que permite repetir a ordem de uma execução.
619. [[rspec-let-let-bang-lazy]] — `let` memoiza um helper quando ele é acessado pela primeira vez em cada exemplo, enquanto `let!` também agenda sua avaliação por um hook antes do exemplo.
### ExUnit — callbacks, concorrência, templates e doctests

620. [[exunit-setup-context-data]] — Callbacks `setup` podem receber contexto e retornar novos valores que são mesclados ao contexto disponível para etapas seguintes e para o teste.
621. [[exunit-setup-all-process-boundary]] — `setup_all` roda uma vez por módulo antes dos testes, em processo separado do processo de cada teste.
622. [[exunit-start-supervised-lifecycle]] — `start_supervised` inicia um processo sob supervisor vinculado ao ciclo de vida do teste e assegura seu encerramento antes de `on_exit`.
623. [[exunit-on-exit-separar-cleanup]] — Callbacks `on_exit` são executados após a saída do processo de teste e rodam em processo separado.
624. [[exunit-async-global-state]] — Com `async: true`, casos de teste podem executar em paralelo com outros módulos, enquanto testes do mesmo módulo permanecem seriais.
625. [[exunit-case-template-reuso]] — `ExUnit.CaseTemplate` permite que módulos de teste usem um template com callbacks e funções comuns.
626. [[exunit-capture-io-isolamento]] — `capture_io` substitui o group leader do processo atual durante a função e devolve o texto capturado.
627. [[exunit-doctest-documentacao]] — `doctest` extrai exemplos formatados na documentação de um módulo e os executa como verificações de comportamento.
628. [[exunit-tags-select-filters]] — Tags associadas a casos ou grupos adicionam metadata ao contexto e podem ser incluídas ou excluídas pela configuração do ExUnit.
629. [[exunit-seed-cases-concorrencia]] — ExUnit permite configurar seed para randomizar testes e `max_cases` para limitar quantos casos de módulos distintos rodam simultaneamente.
### Newman — execução de collections Postman em CLI e CI

630. [[newman-maintenance-workflow-choice]] — O README atual informa que Newman está em modo de manutenção e recomenda Postman CLI para workflows novos que precisem acompanhar recursos recentes.
631. [[newman-collection-source-version]] — `newman run` aceita uma collection exportada em arquivo JSON ou uma URL que forneça a definição da coleção.
632. [[newman-environment-global-precedence]] — O CLI recebe arquivos de environment e globals, e variáveis globais têm precedência inferior às variáveis do environment com o mesmo nome.
633. [[newman-iteration-data-csv-json]] — `--iteration-data` fornece arquivo JSON ou CSV às iterações de uma collection, e `--iteration-count` define a quantidade de execuções quando usado com esses dados.
634. [[newman-folder-selection]] — A opção `--folder` seleciona requests dentro de uma ou mais pastas ou requests nomeadas da collection.
635. [[newman-bail-exit-status]] — `--bail` pode interromper a execução ao encontrar erro em script de teste, e `--suppress-exit-code` substitui o código padrão do runner.
636. [[newman-timeout-scopes]] — Newman configura limites distintos para duração da execução, requests e scripts, que protegem partes diferentes do workflow.
637. [[newman-reporters-artifacts]] — Reporters integrados podem gerar saída terminal, JSON ou JUnit, e selecionar reporters de arquivo pode alterar se o reporter CLI continua habilitado.
638. [[newman-custom-reporter-package]] — Newman pode carregar reporters externos instalados como módulos Node compatíveis com a convenção de reporter.
639. [[newman-programmatic-events-summary]] — A API programática expõe `newman.run`, callback e eventos para iniciar collections de dentro de uma aplicação Node.
### axe-core — escopo de varredura, resultados e limites

640. [[axe-rendered-dom-state]] — axe.run analisa conteúdo renderizado no documento e não avalia automaticamente regiões ocultas que ainda não foram ativadas.
641. [[axe-context-include-exclude]] — O argumento `context` aceita seletores ou nós DOM para incluir regiões e uma configuração de exclusão para omitir áreas escolhidas.
642. [[axe-frames-shadow-dom-context]] — axe-core tem opções de contexto para limitar seleção dentro de frames e de regiões de shadow DOM.
643. [[axe-runonly-tags-rules]] — A opção `runOnly` restringe quais regras ou grupos identificados por tags participam de uma execução.
644. [[axe-result-categories]] — O objeto de resultados separa regras que falharam, passaram, exigem revisão incompleta ou não se aplicam à árvore examinada.
645. [[axe-incomplete-manual-review]] — Uma regra que não consegue decidir automaticamente pode aparecer em `incomplete` com nós que demandam avaliação adicional.
646. [[axe-impact-priorizacao-nao-conformidade]] — O campo `impact` ajuda a ordenar a severidade estimada de uma violação retornada, mas não é certificado de conformidade ou medida completa de impacto ao usuário.
647. [[axe-tags-nao-cobertura-total-wcag]] — Tags de regras identificam relação com versões ou níveis de padrões e também podem marcar melhores práticas, entre outros metadados.
648. [[axe-dynamic-flows-multiple-scans]] — Uma página interativa pode revelar conteúdo novo após abrir modal, menu ou erro de formulário, e cada estado exige uma execução própria para ser observado.
649. [[axe-result-targets-regression]] — Resultados associam violações a nós e alvos, permitindo identificar onde uma regra encontrou o problema na árvore analisada.

## Tranche 13 — frameworks de teste, Rust e execução de suites (IDs 650–749; revisão factual por IA registrada)

### Mocha — interfaces, hooks e execução paralela

650. [[mocha-bdd-suite-tree]] — A interface BDD registra grupos com `describe()` e exemplos individuais com `it()`.
651. [[mocha-hooks-nested-order]] — `before` e `after` envolvem uma suite, enquanto `beforeEach` e `afterEach` acompanham cada teste daquele escopo.
652. [[mocha-async-completion-contract]] — Mocha reconhece teste síncrono, callback `done`, promessa retornada e função `async` que devolve promessa.
653. [[mocha-root-hooks-plugin]] — Um Root Hook Plugin exporta hooks que o Mocha instala fora de uma suite nomeada.
654. [[mocha-parallel-order-isolation]] — Com `--parallel`, Mocha distribui arquivos por workers e não garante a ordem em que eles serão executados.
655. [[mocha-retry-diagnostic]] — A opção `--retries` repete testes que falham até o limite configurado; por padrão, falhas não são repetidas.
656. [[mocha-timeout-test-and-hook]] — Mocha aplica limite de duração a testes e hooks, e o valor pode ser configurado em níveis diferentes.
657. [[mocha-grep-focused-suite]] — `--grep` seleciona testes pelos títulos correspondentes e pode ser usado para executar um recorte sem alterar a suíte.
658. [[mocha-reporter-parallel-output]] — Reporters transformam resultados em saída de terminal ou arquivos, e algumas opções precisam conhecer a suíte inteira antes da execução.
659. [[mocha-global-fixture-lifecycle]] — Global fixtures oferecem configuração e limpeza uma vez para a execução do Mocha, ao passo que hooks pertencem às suites e seus testes.

### Jasmine 7 — spies, relógio simulado e execução assíncrona

660. [[jasmine-promise-completion]] — Jasmine aguarda a promessa retornada por um spec ou hook e falha o spec quando ela rejeita.
661. [[jasmine-done-callback]] — Ao declarar argumento `done`, o spec ou hook usa o callback entregue por Jasmine para sinalizar conclusão.
662. [[jasmine-clock-tick-cleanup]] — `jasmine.clock()` instala relógio simulado que permite avançar timers enfileirados sem esperar tempo real.
663. [[jasmine-mock-date-time]] — O relógio de Jasmine pode ser instruído a simular a data que `new Date()` retorna.
664. [[jasmine-spy-through-vs-stub]] — Um spy pode registrar chamadas e também ser configurado para executar a implementação original ou devolver comportamento falso.
665. [[jasmine-spy-call-history]] — O objeto Spy expõe histórico de chamadas para examinar quantidade, argumentos e ordem observada.
666. [[jasmine-beforeall-state-boundary]] — `beforeAll` prepara uma vez os specs de seu grupo, enquanto `beforeEach` roda antes de cada spec.
667. [[jasmine-focused-spec-cleanup]] — `fit` e `fdescribe` focam uma spec ou suite e fazem com que apenas testes focados sejam executados.
668. [[jasmine-pending-spec-intent]] — Um spec `it` sem função de teste é marcado como pending, e a API também distingue specs focados.
669. [[jasmine-async-matcher-await]] — `expectAsync()` cria expectations cujos matchers retornam promises que precisam ser aguardadas ou retornadas.

### WebdriverIO — espera explícita, runners e isolamento

670. [[webdriverio-auto-wait-interactable]] — Comandos que interagem diretamente com elemento aguardam que ele esteja visível e interagível antes de agir.
671. [[webdriverio-waituntil-condition]] — `browser.waitUntil()` consulta uma condição até que ela retorne valor truthy ou ultrapasse o timeout configurado.
672. [[webdriverio-wait-displayed-state]] — `waitForDisplayed()` aguarda que um elemento esteja exibido, condição diferente de apenas localizar um seletor no DOM.
673. [[webdriverio-soft-assertion-aggregation]] — `expect.soft()` coleta falhas sem interromper imediatamente o teste e as reporta juntas ao final quando o serviço correspondente está ativo.
674. [[webdriverio-local-worker-isolation]] — No Local Runner, cada arquivo de teste roda em processo worker separado por capability, com sua própria sessão de browser.
675. [[webdriverio-browser-runner-boundary]] — Browser Runner executa framework de teste dentro de browser real e é diferente do Local Runner que inicia framework em processo Node.
676. [[webdriverio-selector-contract]] — WebdriverIO aceita estratégias de seletor diferentes, que variam em estabilidade e relação com a interface de usuário.
677. [[webdriverio-capability-concurrency]] — Configuração do runner combina capabilities de browser e limites de execução concorrente.
678. [[webdriverio-spec-file-retries]] — Configuração pode repetir um arquivo de spec que falhou até o limite `specFileRetries`.
679. [[webdriverio-group-spec-execution]] — Suite pode ser organizada em grupos de spec que executam juntos, útil quando uma dependência de execução é inevitável.

### Cargo test e rustdoc — organização e controle de execução

680. [[cargo-unit-test-module]] — Unit tests escritos num módulo `#[cfg(test)]` dentro do arquivo podem acessar itens privados do módulo pai.
681. [[cargo-integration-test-crate]] — Arquivos no diretório superior `tests/` são compilados individualmente como crates de integração.
682. [[rustdoc-compile-fail-doctest]] — A cerca `compile_fail` marca um bloco de documentação que rustdoc compila negativamente e aprova quando o trecho não compila.
683. [[cargo-doctest-hidden-setup]] — Linhas iniciadas por `#` podem compor contexto compilável do doctest sem aparecer no trecho renderizado.
684. [[cargo-test-filter-argument-boundary]] — O argumento de filtro e os parâmetros depois de `--` são encaminhados ao executável de teste, enquanto opções antes do separador pertencem ao Cargo.
685. [[cargo-no-run-compilation-check]] — A opção `--no-run` compila executáveis de teste sem iniciar o harness.
686. [[cargo-no-fail-fast-scope]] — `--no-fail-fast` faz Cargo continuar para executáveis de teste posteriores depois de um deles falhar.
687. [[cargo-test-thread-count-isolation]] — Testes do harness podem rodar em múltiplas threads, e `--test-threads` limita a concorrência desse executável.
688. [[cargo-target-selection]] — Cargo consegue selecionar workspace, pacote, biblioteca, binário, exemplo ou alvo de integração em vez de compilar tudo.
689. [[cargo-harness-false-boundary]] — Alvos com `harness = false` deixam de receber o harness automático e precisam fornecer seu próprio `main` para executar testes.

### Criterion.rs — metodologia, configuração e interpretação de benchmarks

690. [[criterion-benchmark-input-black-box]] — `bench_with_input()` associa um valor de entrada e um identificador ao benchmark e passa o input por `black_box`.
691. [[criterion-benchmark-group-parameters]] — `BenchmarkGroup` relaciona casos que medem a mesma pergunta com parâmetros diferentes e gera sumarização conjunta.
692. [[criterion-throughput-units]] — Throughput em bytes ou elementos exige informar quantos deles são processados em cada iteração.
693. [[criterion-warmup-measurement-phases]] — Execução de benchmark passa por warmup, medição, análise e comparação com resultados salvos.
694. [[criterion-sample-size-tradeoff]] — A quantidade de amostras afeta duração da execução e capacidade de estimar diferenças pequenas com a análise estatística configurada.
695. [[criterion-outlier-interpretation]] — Criterion classifica outliers e avisa sobre sua presença, mas a análise subsequente continua usando as amostras coletadas.
696. [[criterion-baseline-comparison]] — Criterion compara estatísticas atuais com dados previamente salvos e estima se a diferença pode ser atribuída a variação.
697. [[criterion-flat-sampling-long-workload]] — Criterion oferece modos de amostragem `Auto`, `Linear` e `Flat`, sendo o último destinado a benchmarks de longa duração.
698. [[criterion-throughput-and-log-scale]] — Grupos podem descrever throughput e usar escala logarítmica quando tamanhos de input crescem exponencialmente.
699. [[criterion-benchmark-loop-scope]] — A closure de benchmark precisa repetir o trabalho que se deseja medir e evitar que preparação não representativa domine a duração.

### Ginkgo v2 — árvore de specs, paralelismo e confiabilidade

700. [[ginkgo-container-tree]] — Ginkgo usa `Describe`, `Context` e `It` para compor uma árvore de especificações que o runner constrói antes de executar os casos.
701. [[ginkgo-before-after-nesting]] — `BeforeEach` roda para cada spec em seu escopo e hooks aninhados seguem hierarquia do container.
702. [[ginkgo-suite-synchronized-setup]] — Suite-level setup e teardown têm nós próprios; em execução paralela, recurso compartilhado exige coordenação entre processos.
703. [[ginkgo-process-parallel-isolation]] — CLI `ginkgo -p` executa specs usando processos paralelos e acelera suites que não compartilham recurso mutável.
704. [[ginkgo-random-order-seed]] — Randomização muda ordem de execução dos specs e seed permite repetir a sequência que revelou dependência entre casos.
705. [[ginkgo-label-filter]] — Labels associam metadados a specs e filtros permitem selecionar conjuntos sem comentar ou editar a árvore de testes.
706. [[ginkgo-describe-table-entries]] — `DescribeTable` e `Entry` produzem specs a partir de exemplos declarados de forma explícita.
707. [[ginkgo-eventually-context]] — `Eventually` repete observação até matcher passar ou contexto/timeout encerrar a tentativa.
708. [[ginkgo-consistently-window]] — `Consistently` avalia matcher por uma janela temporal para verificar que condição permanece verdadeira ou comportamento indesejado não aparece.
709. [[ginkgo-flake-attempts-evidence]] — `FlakeAttempts` permite executar novamente um spec marcado como flakey até o limite definido.

### ScalaTest 3.2 — estilos, fixtures, tags e tabelas

710. [[scalatest-style-selection]] — ScalaTest oferece style traits que adaptam a forma de declarar testes sem mudar o conceito central de `Suite`.
711. [[scalatest-pending-cancel-semantics]] — Pending indica teste conhecido que ainda não foi implementado, enquanto cancel interrompe execução por condição que impede avaliação naquele contexto.
712. [[scalatest-assertion-clue]] — Assertions ScalaTest podem carregar pistas contextuais para indicar qual etapa ou dado contribuiu para uma falha.
713. [[scalatest-tags-select-test-runs]] — Tags classificam testes e runners permitem incluir ou excluir grupos durante a execução.
714. [[scalatest-runner-entrypoints]] — ScalaTest pode ser executado por frameworks de build, Runner de linha de comando, IDEs e integrações específicas.
715. [[scalatest-fixture-withfixture]] — `withFixture` permite envolver execução de testes com preparação e cleanup comuns a grande parte de uma suite.
716. [[scalatest-loan-fixture-cleanup]] — Loan-fixture é opção quando testes diferentes precisam de objetos específicos que precisam ser limpos ao concluir.
717. [[scalatest-table-driven-check]] — `TableDrivenPropertyChecks` aplica uma propriedade às linhas tipadas de `Table` usando métodos como `forAll` e `forEvery`.
718. [[scalatest-matcher-composition]] — Matchers fornecem linguagem declarativa para comparar estado observado com condição esperada.
719. [[scalatest-async-future-result]] — Estilos assíncronos do ScalaTest integram resultado de teste com `Future` e só concluem quando esse resultado finaliza.

### Spock 2.4 — fixtures, dados e interações

720. [[spock-given-when-then-contract]] — Uma feature Spock pode separar preparação, estímulo e resultado nos blocos `given:`, `when:` e `then:`.
721. [[spock-fixture-lifecycle-order]] — `setupSpec`, `setup`, `cleanup` e `cleanupSpec` cobrem preparação e liberação em escopos diferentes.
722. [[spock-shared-field-scope]] — Campos de instância recebem objeto independente para cada feature; `@Shared` amplia vida útil e partilha objeto entre métodos.
723. [[spock-data-table-iterations]] — Bloco `where:` fornece data variables que executam a mesma feature para cada linha da tabela.
724. [[spock-where-iteration-isolation]] — Cada iteração de feature data-driven ganha instância própria da specification e passa por setup e cleanup.
725. [[spock-mock-interaction-constraints]] — Interação em bloco `then:` descreve chamadas esperadas por cardinalidade, alvo, método e argumentos.
726. [[spock-stub-response-generator]] — Operador `>>` define resposta que mock ou stub fornece quando recebe chamada correspondente.
727. [[spock-lenient-mock-scope]] — Mocks Spock são lenientes por padrão para chamadas inesperadas que não foram descritas, respondendo com valor default.
728. [[spock-exception-condition]] — Condições de Spock ajudam verificar comportamento de exceção no caminho em que ela é lançada.
729. [[spock-extension-boundary]] — Extensions registram comportamento reaproveitável que intercepta ou complementa lifecycle de specs e features.

### GoogleTest — fixtures, parametrização, assertions e gMock

730. [[googletest-test-suite-registration]] — Macro `TEST()` registra função de teste associada a uma suite nomeada, sem exigir lista manual para executar os casos.
731. [[googletest-test-fixture-instance]] — `TEST_F` liga caso a uma classe derivada de `testing::Test`, e cada teste usa objeto fixture próprio.
732. [[googletest-fatal-vs-nonfatal]] — `ASSERT_*` interrompe a função de teste no primeiro erro, enquanto `EXPECT_*` registra falha não fatal e continua.
733. [[googletest-value-parameterized-suite]] — Teste value-parameterized reutiliza um padrão de fixture e executa para valores fornecidos por gerador.
734. [[googletest-typed-test-known-types]] — Typed tests executam o mesmo conjunto de definições para uma lista de tipos conhecida na compilação.
735. [[googletest-type-parameterized-contract]] — Type-parameterized tests definem padrões antes de conhecer a lista concreta de tipos que os instanciará.
736. [[googletest-filter-selected-tests]] — Filtro `--gtest_filter` seleciona suites e testes pelo padrão de nome durante execução.
737. [[googletest-death-test-process]] — Death tests verificam se uma operação encerra ou termina processo segundo condição esperada.
738. [[googletest-global-environment-boundary]] — Test environment oferece `SetUp` e `TearDown` de escopo do programa, diferente de fixture por teste.
739. [[gmock-interaction-expectation]] — `EXPECT_CALL` descreve chamada esperada a mock, incluindo método, argumentos, frequência e resposta opcional.

### CTest e CMake — descoberta, fixtures, filtros e relatórios

740. [[ctest-enable-testing-scope]] — CTest executa testes descritos em `CTestTestfile.cmake`, que CMake gera quando testing foi habilitado no diretório apropriado.
741. [[ctest-add-test-command]] — A assinatura nomeada de `add_test(NAME ... COMMAND ...)` associa identificador estável e comando ao teste executado por CTest.
742. [[ctest-working-directory-contract]] — `WORKING_DIRECTORY` define o diretório de execução do teste; quando omitido, CTest usa diretório binário atual.
743. [[ctest-exit-code-will-fail]] — Por padrão, código de saída zero aprova teste e código diferente de zero o reprova; `WILL_FAIL` inverte essa lógica para casos que esperam retorno de falha.
744. [[ctest-timeout-failure-diagnostic]] — Propriedade TIMEOUT define limite de parede por teste e impede processo travado de bloquear indefinidamente a suite.
745. [[ctest-label-filter]] — Propriedade `LABELS` classifica teste e CTest permite selecionar ou excluir rótulos sem renomear alvo.
746. [[ctest-fixture-dependency-graph]] — `FIXTURES_SETUP` marca um teste preparatório e `FIXTURES_REQUIRED` marca consumidores que precisam daquele recurso.
747. [[ctest-parallel-processors]] — CTest pode executar testes em paralelo, e propriedade PROCESSORS informa quantos slots cada caso consome.
748. [[ctest-repeat-and-random-order]] — CTest oferece opções de repetição e ordem aleatória para exercitar casos várias vezes no mesmo run.
749. [[ctest-junit-preset-output]] — Test Preset guarda opções de execução reutilizáveis e CTest pode gravar saída JUnit com `--output-junit`.

## Tranche 14 — frameworks de build, teste e tooling atuais

### Bazel — testes herméticos, sinais de execução e resultados

750. [[bazel-test-hermetic-runtime-boundary]] — Um teste executado por Bazel deve depender de fontes declaradas, produtos de build declarados e recursos cujo comportamento o runner garante.
751. [[bazel-test-runtime-files-through-runfiles]] — Arquivos usados durante a execução devem chegar ao teste como entradas de runtime do alvo, e não por caminhos presumidos na árvore de saída.
752. [[bazel-test-shard-contract]] — `shard_count` solicita shards, mas cabe ao test runner suportar a partição e usar os índices de shard que o Bazel fornece.
753. [[bazel-test-size-and-timeout]] — `size` informa a demanda de recursos presumida, enquanto `timeout` define a classe de duração; os atributos são relacionados, mas não intercambiáveis.
754. [[bazel-test-output-as-diagnostic-policy]] — `--test_output` controla como stdout e stderr dos testes aparecem durante `bazel test`, com modos úteis para resumo, falhas, tudo ou transmissão ao vivo.
755. [[bazel-test-env-declaration]] — `--test_env` injeta uma variável no ambiente do teste; especificar valor fixa esse valor, enquanto omiti-lo herda o valor do shell que iniciou Bazel.
756. [[bazel-test-arg-forwarding]] — `--test_arg` encaminha argumentos ao programa de teste, permitindo usar filtros próprios sem confundir opções do framework com flags de Bazel.
757. [[bazel-test-target-selection-patterns]] — `bazel test` seleciona regras de teste por labels e padrões de targets, não por nomes internos de métodos de qualquer framework.
758. [[bazel-build-event-protocol-test-results]] — Build Event Protocol representa a invocação como eventos estruturados e inclui resultados e progresso de testes para ferramentas consumidoras.
759. [[bazel-remote-test-environment]] — Execução remota distribui ações de build e teste em workers, portanto o teste não deve depender de estado local não declarado.

### Maven Surefire e Failsafe — ciclo de vida, seleção e isolamento

760. [[maven-surefire-test-phase]] — Surefire executa testes unitários na fase `test` do ciclo Maven e produz relatórios texto e XML no diretório padrão do projeto.
761. [[maven-failsafe-verify-lifecycle]] — Failsafe separa execução de testes de integração em `integration-test` da avaliação final de resultados em `verify`.
762. [[maven-single-test-selection]] — A propriedade `-Dtest` seleciona classes ou métodos para Surefire, e deve ser tratada como filtro de diagnóstico, não como execução integral.
763. [[maven-junit-platform-provider-boundary]] — A integração com JUnit Platform usa engines presentes nas dependências para executar frameworks compatíveis; no Surefire 3.6.0 o provider unificado é documentado.
764. [[maven-test-class-naming-patterns]] — Os padrões de inclusão do Surefire determinam quais classes compiladas entram na execução padrão.
765. [[maven-fork-count-process-isolation]] — `forkCount` limita quantas JVMs de teste são abertas em paralelo; valor zero executa no processo Maven, enquanto valor positivo usa processos separados.
766. [[maven-parallel-tests-thread-safety]] — Surefire não executa testes em paralelo por padrão; paralelismo precisa ser configurado segundo provider e estrutura de testes.
767. [[maven-skip-execution-vs-test-compilation]] — `-DskipTests` pula a execução dos testes, enquanto `-Dmaven.test.skip=true` também pode pular a compilação do código de teste.
768. [[maven-rerun-flaky-evidence]] — `rerunFailingTestsCount` repete falhas até aprovação ou esgotamento e o Surefire marca um caso que passa depois de falhar como flaky.
769. [[maven-failsafe-report-separation]] — Failsafe registra resultados de integração em formato compatível com Surefire, mas seus relatórios ficam em diretório próprio.

### Gradle — tasks Test, suites JVM e isolamento de execução

770. [[gradle-test-task-input-contract]] — Uma task Gradle do tipo `Test` precisa dos diretórios de classes de teste e do classpath de execução para descobrir e executar casos JVM.
771. [[gradle-select-junit-platform-engine]] — Adicionar uma dependência de teste não basta para selecionar o mecanismo de execução; a task `Test` deve usar a plataforma apropriada ao framework.
772. [[gradle-jvm-test-suite-boundary]] — O plugin JVM Test Suite permite agrupar testes por propósito, com source, dependências, framework e task próprios.
773. [[gradle-check-dependency-for-suite]] — Uma suite de teste adicional não passa a rodar em `check` apenas por existir; seu vínculo com o lifecycle deve ser declarado.
774. [[gradle-parallel-forks-and-unique-resources]] — `maxParallelForks` define o máximo de processos de teste concorrentes e seu valor padrão é um.
775. [[gradle-fork-every-process-reset]] — `forkEvery` reinicia o processo de teste depois de certo número de classes ou definições executadas.
776. [[gradle-test-filter-vs-discovery]] — O filtro da task permite reduzir quais testes são executados, enquanto a descoberta identifica classes e métodos reconhecidos pelo framework.
777. [[gradle-fail-on-empty-test-discovery]] — `failOnNoDiscoveredTests` pode impedir que uma task com fontes de teste existentes termine silenciosamente sem descobrir nenhum teste.
778. [[gradle-test-report-artifact-contract]] — Cada task de teste produz resultados que o Gradle pode converter em relatórios, e suites separadas permitem inspecionar resultados por finalidade.
779. [[gradle-ignore-failures-policy]] — `ignoreFailures` permite que o build prossiga após falha da task Test, mas não altera o resultado individual dos testes.

### Django 6.1 — cliente, banco, views e isolamento de settings

780. [[django-testcase-database-isolation]] — `django.test.TestCase` executa cada teste com isolamento transacional e é a base adequada para a maioria dos casos que consultam ou alteram o banco.
781. [[django-client-without-live-server]] — O `django.test.Client` simula requisições à aplicação sem exigir que um servidor de desenvolvimento esteja rodando.
782. [[django-requestfactory-middleware-boundary]] — `RequestFactory` cria objetos request para passar diretamente a uma view, sem executar o ciclo de roteamento e middleware.
783. [[django-setuptestdata-class-fixture]] — `setUpTestData()` prepara dados de banco uma vez por classe `TestCase`, ao passo que `setUp()` roda antes de cada método de teste.
784. [[django-live-server-browser-boundary]] — `LiveServerTestCase` inicia um servidor de teste em thread para permitir que Selenium ou outro cliente real interaja com a aplicação.
785. [[django-assert-num-queries-scope]] — `assertNumQueries` verifica quantas queries SQL foram executadas dentro de um bloco ou por uma operação específica do teste.
786. [[django-email-outbox-testing]] — Durante testes, Django fornece uma caixa de saída em memória para observar mensagens enviadas pelo código da aplicação.
787. [[django-override-settings-scope]] — `override_settings` substitui temporariamente valores de settings e restaura o contexto ao final do escopo gerenciado.
788. [[django-test-discovery-and-labels]] — O comando `manage.py test` descobre por padrão módulos que seguem o padrão de nomes de teste e aceita labels para reduzir o escopo.
789. [[django-client-csrf-enforcement]] — O cliente Django desativa verificações CSRF por padrão, então um POST aceito pelo Client não prova sozinho que a proteção foi aplicada.

### Android Espresso — sincronização, intents, listas e acessibilidade

790. [[espresso-view-action-assertion-chain]] — O fluxo central do Espresso separa a seleção de uma view, a ação do usuário e a assertion sobre o estado apresentado.
791. [[espresso-automatic-idle-boundary]] — Espresso aguarda condições conhecidas da fila de UI e recursos de idling registrados, mas não entende automaticamente toda tarefa de background.
792. [[espresso-register-idling-resource-lifecycle]] — Os benefícios de sincronização começam quando Espresso consulta o recurso; registrar antecipadamente evita uma primeira ação que passe sem observá-lo.
793. [[espresso-intents-validate-outgoing]] — `intended()` verifica se um intent de saída que corresponde ao matcher foi registrado pelo Espresso-Intents.
794. [[espresso-intents-stub-response]] — `intending()` configura uma resposta para intents de saída correspondentes e permite testar o fluxo local sem abrir o aplicativo externo.
795. [[espresso-adapter-view-ondata-selection]] — `onData()` procura o objeto de dados que alimenta uma `AdapterView` e pode rolar a lista até tornar a linha correspondente visível.
796. [[espresso-recyclerview-actions]] — `RecyclerViewActions` oferece ações de lista para localizar e operar itens que podem não estar materializados na tela.
797. [[espresso-accessibility-checks-at-actions]] — `AccessibilityChecks.enable()` integra verificações do Android Accessibility Test Framework às ações de view feitas pelos testes Espresso.
798. [[espresso-suppress-accessibility-narrowly]] — O matcher de supressão deve identificar um finding específico, em vez de silenciar toda uma categoria ou tela.
799. [[espresso-webview-testing-boundary]] — Espresso-Web é apropriado para exercitar o WebView como parte de uma aplicação híbrida e pode ser combinado a operações Espresso em views nativas.

### Rails 8.1 — fixtures, integração HTTP, tempo, jobs e paralelismo

800. [[rails-fixtures-stable-reference-data]] — Fixtures Active Record armazenam dados de teste declarativos e permitem que casos usem um conjunto conhecido de registros.
801. [[rails-test-environment-database-boundary]] — Rails executa testes sob `RAILS_ENV=test` e configura um banco de teste distinto conforme a configuração da aplicação.
802. [[rails-integration-test-full-stack-flow]] — `ActionDispatch::IntegrationTest` exercita vários controllers e o caminho completo entre dispatcher, aplicação e banco.
803. [[rails-integration-json-response-contract]] — `IntegrationTest` permite declarar formato de request e inspecionar corpo parseado para testar um endpoint JSON dentro da aplicação.
804. [[rails-system-test-browser-scope]] — Rails system tests usam Capybara para exercitar a aplicação no browser, inclusive comportamento JavaScript percebido pelo usuário.
805. [[rails-parallel-process-test-isolation]] — Rails pode distribuir testes por processos e criar bancos de teste correspondentes a workers quando a configuração de banco está disponível.
806. [[rails-freeze-time-helper-cleanup]] — `travel_to` e `freeze_time` substituem fontes de tempo relevantes para testar vencimentos e agendamentos sem esperar pelo relógio real.
807. [[rails-activejob-enqueue-vs-perform]] — Active Job oferece helpers de teste para observar jobs enfileirados e executar jobs sob demanda com o adapter de teste.
808. [[rails-mailer-generation-and-delivery-tests]] — Rails oferece testes de mailer para verificar mensagem construída e testes de integração para o fluxo de entrega acionado por outra camada.
809. [[rails-test-file-and-line-selection]] — O comando `bin/rails test` aceita um caminho de teste e seletores mais específicos para encurtar o ciclo de investigação.

### tox 4 — ambientes reproduzíveis, fatores e execução

810. [[tox-toml-over-deprecated-ini]] — tox 4 aceita TOML nativo e mantém INI por compatibilidade, mas a documentação marca INI como obsoleto e congelado.
811. [[tox-env-list-is-default-matrix]] — `env_list` define ambientes que tox seleciona por padrão quando a execução não recebe um escopo mais restrito.
812. [[tox-factor-matrix-combinations]] — Fatores são segmentos do nome do ambiente e permitem condicionar dependências ou comandos por combinação, incluindo plataforma.
813. [[tox-deps-commands-and-posargs]] — Configuração tox define dependências de ambiente e comandos a executar, podendo encaminhar argumentos do usuário ao runner.
814. [[tox-env-selection-sequential-vs-parallel]] — `tox run -e` executa ambientes escolhidos segundo a ordem especificada, enquanto o subcomando `tox parallel` executa em modo concorrente.
815. [[tox-pass-env-explicit-contract]] — `pass_env` seleciona variáveis do ambiente do processo que podem atravessar para a execução do ambiente tox.
816. [[tox-config-command-as-debugging-tool]] — O comando `tox config` mostra valores efetivos de um ambiente, incluindo herança e substituições aplicadas.
817. [[tox-exec-is-not-configured-test-run]] — `tox exec` roda um comando pontual no ambiente selecionado, sem executar `commands`, `commands_pre` ou `commands_post`, e sem instalar pacote.
818. [[tox-parallel-pytest-temp-isolation]] — Quando tox paraleliza ambientes que executam pytest, cada invocação deve usar diretório temporário próprio para evitar colisões.
819. [[tox-package-under-test-contract]] — tox pode preparar um pacote do projeto e instalá-lo no ambiente antes de rodar os comandos configurados.

### Nox — sessões Python, parametrização e seleção de tarefas

820. [[nox-python-version-matrix]] — Uma sessão Nox pode declarar vários intérpretes e gerar uma execução isolada para cada versão suportada.
821. [[nox-parametrize-session-axis]] — `nox.parametrize` expande uma função de sessão em invocações distintas com argumentos definidos pela matriz.
822. [[nox-recreate-vs-reuse-venv]] — Por padrão, Nox recria virtualenvs a cada execução; reuso é opção consciente para acelerar ciclos locais.
823. [[nox-no-virtualenv-scope]] — `python=False` ou backend `none` executa sessão sem criar virtualenv gerenciada pelo Nox.
824. [[nox-default-session-surface]] — Por padrão Nox executa todas as sessões configuradas, a menos que opções ou `default=False` alterem a seleção padrão.
825. [[nox-requires-session-dependency-order]] — `requires` permite que uma sessão dependa de outras, cuja ordem de execução Nox resolve de forma estável e topológica.
826. [[nox-tag-filtered-ci-selection]] — Sessões Nox aceitam tags e a CLI pode filtrar sessões por tags ou expressão de keywords.
827. [[nox-session-install-run-boundary]] — `session.install()` prepara pacotes no ambiente da sessão, enquanto `session.run()` invoca comandos dentro do contexto daquela sessão.
828. [[nox-external-command-boundary]] — `session.run` espera comando disponível no ambiente da sessão; executável do host deve ser autorizado de forma explícita quando necessário.
829. [[nox-posargs-test-filter-forwarding]] — Nox expõe argumentos posicionais da sessão para que o chamador acrescente opções do test runner.

### Laravel 13 — HTTP, banco e fakes de dependências

830. [[laravel-unit-vs-feature-bootstrap]] — Testes Unit não iniciam a aplicação Laravel e por isso não acessam automaticamente banco ou serviços do framework; Feature tests podem atravessar objetos e requests HTTP.
831. [[laravel-testing-environment-boundary]] — Laravel configura ambiente de teste por meio da configuração de PHPUnit e fornece arquivo `.env.testing` para valores específicos de teste.
832. [[laravel-refresh-database-transaction-contract]] — `RefreshDatabase` limpa o estado entre testes e, se o schema já estiver atualizado, executa o teste em transação sem migrar novamente.
833. [[laravel-http-test-internal-request]] — Os métodos de HTTP tests exercitam a aplicação sem emitir uma requisição real pela rede e retornam uma resposta de teste com assertions.
834. [[laravel-json-path-assertions]] — Fluent JSON assertions permitem verificar caminho, estrutura e valores selecionados sem fixar detalhes irrelevantes do documento completo.
835. [[laravel-http-client-fake-prevent-network]] — `Http::fake` substitui respostas de saída do HTTP client Laravel e pode evitar que teste faça requests para serviços externos.
836. [[laravel-event-fake-scope]] — Fakes de eventos permitem verificar dispatch sem executar listeners reais que podem enviar notificações, chamar rede ou alterar outros sistemas.
837. [[laravel-queue-fake-job-contract]] — `Queue::fake()` permite inspecionar jobs enviados à fila sem iniciar worker nem usar o backend real.
838. [[laravel-mail-fake-content-vs-delivery]] — `Mail::fake()` registra mailables enviados para que testes verifiquem destinatário e conteúdo sem acessar transporte externo.
839. [[laravel-parallel-test-database-tokens]] — Ao executar testes em paralelo, Laravel cria e migra bancos de teste por processo usando um token único no nome.

### Python unittest — descoberta, fixtures, subtests e mocks

840. [[python-unittest-discovery-names]] — `unittest` descobre métodos pelo padrão `test` e o discovery recursivo usa convenções de nomes de arquivos e pacotes.
841. [[python-unittest-subtest-dimensions]] — `subTest()` marca uma subexecução com parâmetros durante o mesmo método e permite identificar qual combinação falhou.
842. [[python-unittest-setuptestdata-lifecycle]] — `setUp()` e `tearDown()` executam em torno de cada método de teste, enquanto setup de classe é compartilhado por métodos da mesma classe.
843. [[python-unittest-addcleanup-lifo]] — `addCleanup()` registra funções que rodam em ordem inversa de registro ao finalizar o caso, inclusive quando `setUp()` falha depois do registro.
844. [[python-unittest-assert-raises-regex]] — `assertRaisesRegex` verifica que uma chamada lança o tipo de exceção esperado e que sua mensagem combina com uma expressão regular.
845. [[python-unittest-skip-vs-expected-failure]] — Skip remove temporariamente um teste da execução com motivo; `expectedFailure` marca que o caso deve falhar e registra sucesso inesperado como resultado distinto.
846. [[python-mock-patch-lookup-namespace]] — `patch()` substitui um objeto no namespace em que o código sob teste procura o nome, não necessariamente onde a classe foi originalmente definida.
847. [[python-mock-autospec-interface-check]] — `autospec` cria mocks guiados pela assinatura ou interface do objeto real e pode rejeitar atributos que não existem.
848. [[python-isolated-asyncio-testcase-lifecycle]] — `IsolatedAsyncioTestCase` permite escrever setup, teste e teardown assíncronos mantendo o contrato de TestCase.
849. [[python-unittest-assertlogs-context]] — `assertLogs()` captura registros de logging de um logger durante um bloco e permite verificar nível e conteúdo sem interceptar stdout.

## Tranche 15 — frameworks, mocks, cobertura e automação móvel

### Puppeteer — locators, avaliação, rede, protocolos e evidências

850. [[puppeteer-locator-auto-waiting]] — Um locator representa um elemento que pode ainda não existir e só resolve sua localização quando uma ação ou condição é solicitada por meio dele.
851. [[puppeteer-page-evaluate-serialization]] — `page.evaluate()` executa uma função dentro do navegador e devolve apenas valores serializáveis para o processo Node que controla a automação.
852. [[puppeteer-selector-syntax-beyond-css]] — Além de seletores CSS, o Puppeteer aceita extensões como `::-p-text()`, `::-p-aria()` e o combinador `>>>` para atravessar shadow roots abertos.
853. [[puppeteer-network-interception-cooperative]] — Com a interceptação ativa, mais de uma callback pode opinar sobre a mesma requisição, e a resolução cooperativa decide o resultado pela prioridade informada em cada voto.
854. [[puppeteer-request-abort-and-continue]] — Cada requisição capturada precisa terminar em `continue`, `abort` ou `respond`; enquanto isso não acontece, a navegação permanece pendente aguardando a decisão.
855. [[puppeteer-bidi-vs-cdp]] — O Puppeteer controla navegadores por DevTools Protocol ou por WebDriver BiDi, com BiDi como padrão no Firefox e CDP ainda como padrão no Chrome.
856. [[puppeteer-headless-modes]] — O modo headless moderno é o padrão de lançamento, e o binário reduzido `chrome-headless-shell` é solicitado com `headless: 'shell'`, enquanto `headless: false` abre a janela para depuração.
857. [[puppeteer-navigation-race-free]] — Uma ação que dispara navegação deve ser aguardada em conjunto com a espera pelo resultado, para que o observador exista antes de o evento acontecer.
858. [[puppeteer-screenshots-artifacts]] — `page.screenshot()` grava imagem da viewport, da página inteira ou de uma região delimitada, servindo como evidência de falha e insumo de comparação visual.
859. [[puppeteer-browser-context-isolation]] — Cada contexto de navegador mantém cookies, cache e armazenamento próprios, funcionando como um perfil isolado dentro da mesma instância de navegador.

### Mock Service Worker 2 — handlers, respostas, ciclo de vida e padrões de rede

860. [[msw-setupserver-node-interception]] — `setupServer` configura a interceptação de requisições no processo Node sem abrir porta ou servidor real, aplicando os mesmos handlers usados no navegador.
861. [[msw-lifecycle-listen-reset-close]] — O ciclo recomendado inicia a interceptação antes de todos os testes, remove handlers adicionados por cada caso e encerra o servidor ao final da suíte.
862. [[msw-onunhandledrequest-fail]] — Por padrão, uma requisição sem handler correspondente gera aviso; a opção `onUnhandledRequest` permite elevá-la a erro ou fornecer tratamento próprio.
863. [[msw-handler-order-and-overrides]] — As requisições percorrem a lista de handlers em ordem até o primeiro que produzir uma instrução, e `server.use()` insere novos handlers no início da lista.
864. [[msw-passthrough-real-response]] — Retornar `passthrough()` executa a requisição original e devolve a resposta real, e ainda assim a requisição é considerada tratada para fins de resolução.
865. [[msw-httpresponse-construction]] — `HttpResponse` oferece métodos como `json`, `text`, `html` e `error` para compor status, cabeçalhos e corpo da resposta mockada de forma tipada.
866. [[msw-url-patterns-and-params]] — Padrões de URL podem incluir parâmetros de caminho como `:id`, curingas e expressões, e o resolver recebe os valores extraídos para montar a resposta.
867. [[msw-async-handler-and-body]] — Ler o corpo com `await request.json()` exige um resolver assíncrono; um resolver síncrono que tenta aguardar o corpo devolve resultado indefinido.
868. [[msw-shared-handlers-across-environments]] — A mesma lista de handlers pode atender testes automatizados, desenvolvimento local e catálogo de componentes, mantendo uma única descrição do comportamento simulado.
869. [[msw-per-test-error-overrides]] — Um teste específico pode registrar handlers de falha com `server.use()`, substituindo temporariamente o caminho feliz sem alterar a definição global.

### Supertest — requisições HTTP, agentes, asserções e ciclo do servidor

870. [[supertest-agent-persistent-cookies]] — `request.agent(app)` mantém os cookies recebidos entre chamadas, reproduzindo o comportamento de um cliente que preserva sessão entre requisições.
871. [[supertest-chained-expectations]] — O método `expect` permite afirmar status, cabeçalhos e corpo em uma única cadeia encadeada à requisição, com falha apontando a expectativa violada.
872. [[supertest-send-json-body]] — Chamar `.send()` com um objeto faz o Superagent serializar o conteúdo como JSON e definir o cabeçalho de tipo de conteúdo correspondente.
873. [[supertest-end-callback-error-handling]] — O método `end` recebe callback com erro e resposta e pode ser usado quando o teste precisa de controle explícito, enquanto o estilo de promessa cobre a maioria dos casos.
874. [[supertest-multipart-attach]] — O método `attach` adiciona uma parte de arquivo a uma requisição multipart, recebendo caminho do documento e campos adicionais do formulário.
875. [[supertest-auth-headers-set]] — O método `set` adiciona cabeçalhos à requisição e é o caminho para enviar token de portador, chave de API ou cabeçalhos condicionais específicos do caso.
876. [[supertest-timeouts]] — O cliente herdado do Superagent permite configurar tempo limite por resposta ou por prazo total, evitando que uma suíte fique pendurada indefinidamente.
877. [[supertest-binary-buffer-parsing]] — Respostas que não são JSON chegam ao teste como fluxo ou buffer, e a verificação precisa olhar bytes e cabeçalhos em vez de assumir corpo estruturado.
878. [[supertest-server-lifecycle]] — Ao receber a aplicação, o Supertest inicia um servidor em porta efêmera para a requisição e o encerra ao final, dispensando gerenciamento manual de porta na maioria dos casos.
879. [[supertest-against-express-router]] — O Supertest aceita a aplicação completa, um roteador ou uma função de tratamento, e a escolha define quais camadas — parsing, autenticação, middleware — participam do teste.

### Minitest — asserções, spec, mocks, ciclo de vida e paralelização

880. [[minitest-test-class-method-naming]] — Casos escritos em classes que herdam de `Minitest::Test` são descobertos pelos métodos cujo nome começa com `test_`, sem registro manual de suíte.
881. [[minitest-core-assertions]] — O módulo de asserções cobre igualdade, predicados, tipos, inclusão e referência, cada uma produzindo mensagem de falha específica para o tipo de comparação.
882. [[minitest-assert-raises]] — `assert_raises` falha se o bloco não levantar uma das exceções esperadas e devolve a exceção capturada para verificação de mensagem e atributos.
883. [[minitest-setup-teardown]] — Os métodos `setup` e `teardown` executam antes e depois de cada teste da classe, mantendo o estado de preparação isolado entre casos individuais.
884. [[minitest-spec-dsl]] — `Minitest::Spec` oferece `describe` e `it` com hooks `before`, `after` e `around`, além de matchers de expectativa para testes escritos em estilo de especificação.
885. [[minitest-mock-and-stub]] — `Minitest::Mock` registra expectativas e verifica chamadas ao final do teste, enquanto o método `stub` substitui um objeto por um retorno controlado durante o bloco.
886. [[minitest-parallelize-me]] — `parallelize_me!` executa os testes da classe em várias threads, reduzindo tempo total quando os casos são independentes entre si.
887. [[minitest-random-order-and-seed]] — O Minitest executa os testes em ordem aleatória por padrão e informa a semente usada, permitindo repetir a mesma sequência em caso de falha.
888. [[minitest-skip-and-flunk]] — `skip` interrompe o caso com motivo e o registra como pulado, enquanto `flunk` falha de propósito para marcar um caminho que nunca deveria ser alcançado.
889. [[minitest-reporters-and-run]] — O Minitest pode ser executado com `ruby -Ilib:test` em arquivos isolados, com `ruby -e` para carregar toda a suíte ou por integração com Rake e ferramentas de relatório.

### JaCoCo — agente, contadores, relatórios, verificação e instrumentação offline

890. [[jacoco-agent-on-the-fly]] — O agente do JaCoCo instrumenta classes em tempo de execução e grava os dados coletados em um arquivo binário de execução durante a JVM.
891. [[jacoco-counters-meaning]] — O JaCoCo contabiliza instruções, ramos, linhas, complexidade, métodos e classes, cada qual respondendo a uma pergunta distinta sobre a execução.
892. [[jacoco-branch-vs-line]] — A cobertura de ramos mede quantos desfechos de estruturas condicionais foram executados, incluindo os caminhos de `if` e de `switch`.
893. [[jacoco-report-formats]] — O goal de relatório gera HTML para leitura humana e pode produzir XML e CSV para consumo por outras ferramentas, todos derivados do mesmo arquivo de execução.
894. [[jacoco-check-rules-limits]] — O goal de verificação avalia regras compostas por elemento, contador, valor e limite, e pode interromper o build quando o mínimo configurado não é atingido.
895. [[jacoco-offline-instrumentation]] — Na instrumentação offline, as classes são transformadas antes da execução e os dados são gravados pela biblioteca de runtime, sem agente anexado à JVM.
896. [[jacoco-merge-exec-files]] — Quando a suíte roda em várias JVMs, cada processo gera dados próprios, e o goal de merge combina os arquivos em um único conjunto antes do relatório.
897. [[jacoco-excludes-filtering]] — Exclusões podem ser configuradas por classe, pacote, anotação ou expressão, removendo do relatório código que não é alvo de teste significativo.
898. [[jacoco-thresholds-policy]] — Cobertura descreve o que foi executado e não prova qualidade das asserções, portanto o limite deve expressar uma política de proteção contra regressão.
899. [[jacoco-build-integration]] — A integração típica encadeia preparação do agente, execução dos testes, geração de relatório e verificação, cada passo dependendo do anterior no ciclo do projeto.

### Maestro — fluxos YAML, comandos, tags, reuso e evidências

900. [[maestro-flow-yaml-structure]] — Um fluxo do Maestro é um arquivo YAML com identificador do aplicativo no cabeçalho, separador de documento e uma lista de comandos executados em ordem.
901. [[maestro-launch-and-state]] — `launchApp` inicia o aplicativo, `clearState` remove dados persistidos e `stopApp` encerra a execução, permitindo controlar o estado inicial de cada cenário.
902. [[maestro-tapon-selectors]] — O comando `tapOn` aceita texto visível, identificador de testabilidade e posição relativa, e a escolha do seletor define a estabilidade do passo.
903. [[maestro-assertions-and-waits]] — `assertVisible` e `assertNotVisible` verificam o estado da tela, e `extendedWaitUntil` aguarda uma condição com tempo limite antes de seguir.
904. [[maestro-runflow-subflows]] — O comando `runFlow` executa comandos de outro arquivo, aceita variáveis de ambiente e pode ser condicionado à visibilidade de um elemento.
905. [[maestro-input-and-keyboard]] — `inputText` digita em um campo focado, `eraseText` remove caracteres e `hideKeyboard` fecha o teclado virtual quando ele cobre a interface.
906. [[maestro-tags-and-filters]] — Tags declaradas no fluxo permitem selecionar subconjuntos na CLI com `--include-tags` e excluir grupos com `--exclude-tags`, usando lógica de união dentro de cada flag.
907. [[maestro-repeat-and-conditions]] — O comando `repeat` executa um bloco por número de vezes ou enquanto uma condição for verdadeira, permitindo cobrir listas e tentativas sem duplicar comandos.
908. [[maestro-screenshots-artifacts]] — O comando `takeScreenshot` e o diretório de saída da CLI registram imagens dos passos, e a execução pode produzir resultado em formato consumível pelo pipeline.
909. [[maestro-wait-animation-and-scroll]] — `waitForAnimationToEnd` aguarda a interface estabilizar e `scrollUntilVisible` rola a tela até o elemento aparecer, com limite de rolagem.

### Karate — feature files, asserções, configuração, paralelismo e mocks

910. [[karate-gherkin-builtin-steps]] — Arquivos de feature usam sintaxe Gherkin, mas os passos de HTTP, asserção e manipulação de dados já vêm implementados no framework.
911. [[karate-match-assertions]] — O comando `match` compara respostas com valores esperados e aceita marcadores como `#string`, `#number` e `#[]` para validar estrutura sem fixar conteúdo volátil.
912. [[karate-config-js]] — O arquivo `karate-config.js` é avaliado antes das features e devolve um objeto de configuração que pode variar conforme o ambiente selecionado.
913. [[karate-call-and-read]] — `call` executa outra feature como função em contexto isolado, `callonce` reaproveita o resultado e `read` carrega conteúdo de arquivo para os dados do cenário.
914. [[karate-parallel-runner]] — O runner do Karate executa features em paralelo por padrão quando configurado com um número de threads, mantendo cada cenário em contexto isolado.
915. [[karate-data-driven]] — Cenários podem ser repetidos com conjuntos de dados declarados em tabelas, `Examples` ou arquivos externos como CSV, mantendo a lógica única e os dados separados.
916. [[karate-tags-selection]] — Tags declaradas em features e cenários permitem selecionar subconjuntos por execução, incluindo ou excluindo grupos conforme a necessidade do pipeline.
917. [[karate-mock-server]] — O servidor mock do Karate descreve rotas, respostas e validações em feature files, cobrindo contratos antes de o serviço real existir.
918. [[karate-print-and-debug]] — O comando `print` exibe valores no relatório e a resposta completa pode ser inspecionada para diagnóstico quando a asserção falha.
919. [[karate-reports-artifacts]] — O runner gera relatório HTML com o detalhamento de cada feature, cenário e passo, além de artefatos consumíveis por ferramentas de integração contínua.

### Swift Testing — macros, suítes, traits, parametrização e migração

920. [[swift-testing-test-macro]] — A macro `@Test` identifica uma função de teste, dispensando herança de classe e o prefixo `test` no nome do método.
921. [[swift-testing-expect-and-require]] — `#expect` registra uma falha e continua a execução, enquanto `#require` interrompe o teste ao falhar e devolve o valor desembrulhado.
922. [[swift-testing-suites-and-lifecycle]] — Qualquer tipo que contenha funções de teste forma uma suíte, e a anotação `@Suite` é necessária apenas para nome, traits ou agrupamento explícito.
923. [[swift-testing-parameterized-tests]] — A macro `@Test(arguments:)` executa a mesma função para cada argumento, gerando um resultado pai com um filho por valor ou combinação.
924. [[swift-testing-traits]] — Traits são valores aplicados a testes e suítes para desabilitar, condicionar, limitar tempo, marcar tags e registrar referências de defeito.
925. [[swift-testing-tags]] — Tags declaradas em extensões do tipo `Tag` permitem rotular testes e suítes para organização e filtragem em planos de teste.
926. [[swift-testing-serialized]] — Testes rodam em paralelo por padrão e a trait `.serialized` restringe a execução de uma suíte à ordem sequencial.
927. [[swift-testing-async-tests]] — Funções de teste podem ser `async` e aguardar operações diretamente, sem expectativas de inversão de controle nem callbacks de conclusão.
928. [[swift-testing-migration-from-xctest]] — A migração converte classes `XCTestCase` em suítes, métodos com prefixo em funções `@Test` e asserções específicas nas macros de expectativa.
929. [[swift-testing-swift-test-cli]] — O comando `swift test` do SwiftPM descobre e executa os testes do pacote, incluindo os escritos com Swift Testing em toolchains compatíveis.

### MSTest — estrutura, dados, ciclo de vida, paralelização e configuração

930. [[mstest-testclass-and-testmethod]] — Métodos de teste são marcados com `[TestMethod]` dentro de classes anotadas com `[TestClass]`, e precisam ser públicos, de instância e sem parâmetros fora de casos com dados.
931. [[mstest-datarow-inline]] — O atributo `[DataRow]` declara valores constantes para os parâmetros do teste, e cada linha gera uma execução independente identificada pelos dados.
932. [[mstest-dynamicdata-provider]] — O atributo `[DynamicData]` referencia uma propriedade ou método que devolve uma coleção de linhas, permitindo dados calculados ou objetos tipados.
933. [[mstest-lifecycle-order]] — A inicialização e a limpeza acontecem em níveis de assembly, classe e teste, e o nível de teste se repete para cada linha de dados parametrizados.
934. [[mstest-testcontext]] — O executor injeta um objeto `TestContext` no teste, oferecendo informações de execução, resultado da linha de dados e saída de diagnóstico associada ao caso.
935. [[mstest-assertions-and-exceptions]] — O tipo `Assert` reúne comparações de igualdade, verificações de coleção e asserções de exceção que falham com mensagem específica.
936. [[mstest-parallelization]] — A paralelização pode ser declarada por atributo de assembly com escopo e número de trabalhadores, ou configurada globalmente em runsettings ou testconfig.
937. [[mstest-timeout-and-retry]] — Atributos de tempo limite e de repetição permitem interromper operação longa e repetir um caso falho antes de considerá-lo reprovado.
938. [[mstest-categories-and-filtering]] — Atributos de categoria e propriedade rotulam testes para filtragem no executor, permitindo selecionar subconjuntos por tipo ou risco.
939. [[mstest-runsettings-vs-testconfig]] — Executores baseados na plataforma de testes leem `testconfig.json`, enquanto o caminho clássico usa `.runsettings` para paralelização, timeouts e demais ajustes.

### cargo-nextest — isolamento, perfis, retries, partições e relatórios

940. [[nextest-process-per-test]] — O nextest agenda cada teste como um processo separado, em vez de compartilhar o binário de teste entre vários casos como faz o executor padrão.
941. [[nextest-profiles]] — Configurações ficam em arquivo de perfil no workspace, com um perfil padrão e perfis nomeados que podem ser selecionados na linha de comando.
942. [[nextest-retries-and-flaky-result]] — Retries configuram quantas vezes um teste falho é repetido, e a política de resultado define se a execução final conta como falha ou como instável.
943. [[nextest-slow-timeout]] — O limite de lentidão avisa quando um teste excede o período configurado e pode encerrá-lo após um número de períodos.
944. [[nextest-filtersets]] — Expressões de filtro permitem selecionar casos por nome, pacote, tipo de teste e outras propriedades diretamente na linha de comando.
945. [[nextest-partitioning]] — O particionamento divide os testes em fatias ou por hash de identificador, permitindo distribuir a mesma suíte entre executores paralelos.
946. [[nextest-junit-report]] — O nextest pode gravar relatório JUnit XML por perfil, com opções para incluir ou omitir saída de testes aprovados e para classificar resultados instáveis.
947. [[nextest-archives]] — O comando de arquivamento empacota os binários de teste compilados para que outra etapa ou máquina execute o mesmo build sem recompilar.
948. [[nextest-doctests-boundary]] — O nextest executa binários de teste compilados e não cobre exemplos de documentação, que continuam precisando do comando clássico do Cargo.
949. [[nextest-listing-and-ignored]] — O comando de listagem mostra o conjunto descoberto sem executar, e a opção de execução de ignorados permite rodar casos marcados como pendentes.

## Tranche 16 — desempenho, cobertura, acessibilidade e contratos

### Detox — testes end-to-end de React Native com sincronização de dispositivo

950. [[detox-synchronization-gray-box]] — O Detox observa rede, temporizadores e animações do aplicativo e espera a estabilização antes de executar cada ação ou asserção.
951. [[detox-testid-selectors]] — Matchers baseados em identificador procuram o valor de testabilidade definido no componente, enquanto texto e rótulo dependem de conteúdo visível.
952. [[detox-launchapp-options]] — A chamada de lançamento aceita opções como instância nova, permissões de sistema, argumentos e abertura por link, definindo o estado inicial do cenário.
953. [[detox-reload-react-native]] — A recarga do pacote JavaScript restaura o estado da aplicação sem reconstruir o binário nem reiniciar o processo nativo, reduzindo o tempo entre casos.
954. [[detox-waitfor-explicit]] — A espera explícita por um elemento aceita limite de tempo e pode rolar uma lista até o alvo aparecer, cobrindo eventos que a sincronização padrão não acompanha.
955. [[detox-assertions-visibility-existence]] — As asserções de visibilidade verificam o que está apresentado na tela, enquanto as de existência apenas confirmam que o elemento está montado na hierarquia.
956. [[detox-disable-synchronization-scope]] — A sincronização pode ser desativada e reativada durante o teste, delimitando um trecho em que a ferramenta não aguarda operações pendentes.
957. [[detox-device-actions]] — Ações de dispositivo cobrem operações fora da árvore de interface, como enviar o aplicativo ao segundo plano, retomá-lo e capturar a tela em um ponto nomeado.
958. [[detox-artifacts-failure]] — A execução pode capturar telas e gravar vídeos nos casos que falham, produzindo evidência sem exigir reprodução local do problema.
959. [[detox-configuration-file]] — O arquivo de configuração declara aplicativos, dispositivos e configurações nomeadas usadas pelos comandos de build e de teste.
960. [[detox-ci-stability]] — Ambientes de integração contínua sofrem com animações habilitadas, emuladores lentos e recursos limitados, o que altera o tempo das transições.

### Artillery — fases de carga, cenários HTTP e limites de desempenho

961. [[artillery-load-phases]] — Cada fase informa duração e taxa de chegada de usuários virtuais, e a opção de progressão transforma a taxa inicial em taxa final ao longo do período.
962. [[artillery-scenario-flow]] — O bloco de cenários descreve a sequência de passos que cada usuário virtual executa, incluindo requisições, pausas e agrupamentos.
963. [[artillery-capture-and-reuse]] — Valores extraídos da resposta podem ser guardados em variáveis nomeadas e reutilizados nos passos seguintes do mesmo cenário.
964. [[artillery-thresholds]] — A extensão de verificação compara métricas da execução com limites declarados e encerra com código de erro quando algum deles é ultrapassado.
965. [[artillery-metrics-interpretation]] — Durante a execução a ferramenta publica resumo periódico, e ao final apresenta contagens de cenários, requisições, taxas e distribuição de latência.
966. [[artillery-browser-engine]] — Além de requisições HTTP, a ferramenta aceita mecanismo que controla navegador real, permitindo medir carregamento completo de páginas sob carga.
967. [[artillery-expect-plugin]] — A extensão de asserções permite declarar condições sobre cada resposta, como código de status e campo do corpo, falhando o passo quando o contrato não é atendido.
968. [[artillery-quick-and-run]] — O comando de execução rápida parte de um alvo e gera um cenário mínimo para verificação imediata, enquanto a execução por arquivo usa a definição completa.
969. [[artillery-scenario-weights]] — Cenários podem receber pesos relativos, fazendo com que a carga gerada combine jornadas distintas na proporção declarada.
970. [[artillery-rate-vs-concurrency]] — A ferramenta modela taxa de chegada de usuários virtuais ao longo do tempo, e não uma quantidade fixa de requisições por segundo.
971. [[artillery-ci-integration]] — A execução pode gravar o resumo em arquivo e devolver código de erro pelos limites, permitindo que a verificação de desempenho participe do fluxo automático.

### Vegeta — ataques HTTP de taxa constante, relatórios e análise

972. [[vegeta-attack-basics]] — O subcomando de ataque recebe alvos, uma taxa em requisições por segundo e uma duração, emitindo um fluxo binário com os resultados.
973. [[vegeta-targets-file]] — O arquivo de alvos contém método e URL por linha, aceitando cabeçalhos adicionais no bloco seguinte e referência a arquivo de corpo para requisições que enviam dados.
974. [[vegeta-report-metrics]] — O subcomando de relatório resume o fluxo de resultados com latências por percentil, taxa efetiva, volume de dados e proporção de sucesso.
975. [[vegeta-plot-timeline]] — O subcomando de gráfico gera uma página com série temporal de latências, permitindo correlacionar picos com eventos ocorridos durante o ataque.
976. [[vegeta-encode-and-dump]] — Os subcomandos de codificação e descarga convertem o fluxo binário em formatos legíveis, como JSON e CSV, permitindo consumo por ferramentas de análise.
977. [[vegeta-rate-workers-connections]] — A taxa define quantas requisições iniciar por segundo, os trabalhadores definem o paralelismo inicial e as conexões limitam conexões ociosas por host.
978. [[vegeta-timeouts-and-transport]] — O ataque aceita tempo limite por requisição, conexões persistentes, negociação de versão do protocolo e opções de certificado para ambientes de teste.
979. [[vegeta-thresholds-in-ci]] — O relatório pode ser emitido em formato estruturado, o que permite extrair percentuais e proporções e reprovar a execução quando os valores desviam do esperado.
980. [[vegeta-library-usage]] — A ferramenta expõe biblioteca em Go que permite definir alvos dinâmicos, alimentar dados variáveis e consumir resultados no mesmo processo.
981. [[vegeta-load-model-limits]] — O ataque mantém taxa fixa de início de requisições, comportamento que difere de sistemas reais com usuários que esperam respostas antes de agir.

### JMH — microbenchmarks de JVM com aquecimento, estados e modos de medição

982. [[jmh-benchmark-annotation]] — O método anotado como benchmark é envolvido em código gerado que executa e mede repetidamente a mesma operação.
983. [[jmh-blackhole-consumption]] — A estrutura oferece objeto de consumo que registra o valor produzido, impedindo que o compilador remova o cálculo por falta de uso aparente.
984. [[jmh-modes]] — Os modos disponíveis medem vazão por unidade de tempo, tempo médio por operação, amostragem de distribuição e execução única.
985. [[jmh-warmup-and-measurement]] — As anotações definem quantas iterações preparam a máquina virtual e quantas produzem os números que entram no relatório.
986. [[jmh-forking]] — O parâmetro de fork define quantos processos independentes executam o benchmark, cada um com sua própria máquina virtual.
987. [[jmh-state-scope]] — O escopo do objeto de estado define se os dados são compartilhados entre threads, exclusivos de cada thread ou limitados a um grupo.
988. [[jmh-setup-and-teardown]] — A preparação e a limpeza podem ocorrer uma vez por execução, por iteração ou por invocação, conforme o nível escolhido.
989. [[jmh-parameters]] — Campos anotados como parâmetros recebem cada valor declarado, e o benchmark é expandido em uma execução por combinação de valores.
990. [[jmh-profiling-aids]] — A execução aceita perfis embutidos, como contabilização de coleta de lixo, e permite escolher perfiladores externos por linha de comando.
991. [[jmh-execution-and-pitfalls]] — A ferramenta pode ser executada por linha de comando a partir de artefato construído ou por chamada programática em método principal.

### coverage.py — execução instrumentada, ramos, configuração e relatórios

992. [[coveragepy-run-basics]] — O comando de execução instrumenta o interpretador, roda o módulo ou script indicado e grava os dados coletados em arquivo.
993. [[coveragepy-branch-coverage]] — Com cobertura de ramos ativa, a medição registra quais desfechos de decisões foram executados, inclusive caminhos parciais de expressões lógicas.
994. [[coveragepy-config-files]] — As opções podem ser declaradas em arquivo próprio, no arquivo de configuração do projeto ou no empacotamento, com precedência definida.
995. [[coveragepy-omit-and-exclude]] — Padrões de omissão removem arquivos inteiros da medição, e comentários ou expressões de exclusão removem linhas específicas do cálculo.
996. [[coveragepy-parallel-and-combine]] — O modo paralelo faz cada processo gravar arquivo próprio, e os arquivos podem ser combinados antes da geração dos relatórios.
997. [[coveragepy-fail-under]] — A opção de limite mínimo faz o comando terminar com código de erro quando o total fica abaixo do valor definido, tanto na configuração quanto na linha de comando.
998. [[coveragepy-report-formats]] — A ferramenta gera resumo em terminal, página navegável, formato estruturado e formato de intercâmbio, todos derivados dos mesmos dados.
999. [[coveragepy-contexts]] — Cada execução pode receber um rótulo e os relatórios podem filtrar por expressão sobre esses contextos, distinguindo o que cada tipo de teste cobre.
1000. [[coveragepy-subprocesses]] — Processos filhos iniciados durante a execução só são medidos quando a instrumentação é propagada por configuração de ambiente ou por opção de simultaneidade.
1001. [[coveragepy-limits-and-quality]] — Percentual de linhas e ramos descreve o que foi executado, sem atestar que as asserções verificam o comportamento correto.

### nyc e Istanbul — instrumentação JavaScript, limites e consolidação

1002. [[nyc-wrap-command]] — A ferramenta envolve o comando informado, instrumentando os módulos carregados durante a execução e gravando dados brutos em diretório temporário.
1003. [[nyc-all-and-filters]] — A opção de instrumentar tudo faz a medição abranger arquivos que a suíte não carregou, e os filtros de inclusão e exclusão delimitam esse conjunto.
1004. [[nyc-negated-excludes]] — Na lista de exclusão, um padrão iniciado por exclamação restaura caminhos que seriam removidos pela regra anterior ou padrão.
1005. [[nyc-reporters]] — A lista de geradores define os formatos produzidos, e o diretório de relatórios concentra os artefatos publicados.
1006. [[nyc-check-coverage-thresholds]] — A verificação de cobertura compara cada métrica com o limite declarado e encerra com erro quando algum valor fica abaixo do mínimo.
1007. [[nyc-temp-dir-and-merge]] — Os dados brutos ficam no diretório temporário, e a ferramenta permite mesclar arquivos de execuções distintas antes de gerar o relatório consolidado.
1008. [[nyc-typescript-and-source-maps]] — Quando o teste executa código traduzido, os relatórios precisam mapear posições de volta ao original para apontar linhas úteis.
1009. [[nyc-project-root-and-monorepo]] — A raiz do projeto orienta a busca de fontes, a formação de padrões e a localização dos diretórios de artefato.
1010. [[nyc-ci-multi-job]] — Cada trabalho do pipeline publica seu diretório de dados brutos como artefato, e uma etapa final baixa todos, mescla e publica o resultado consolidado.
1011. [[nyc-excludes-and-generated-code]] — Artefatos produzidos por geradores de contrato e de esquema entram na medição quando os padrões não os alcançam.
1012. [[nyc-interpreting-numbers]] — Statements, branches, functions e lines medem dimensões distintas, e um arquivo pode estar integralmente coberto em uma delas e descoberto em outra.

### Lighthouse CI — coleta, asserções, orçamentos e publicação de métricas web

1013. [[lighthouseci-autorun-steps]] — O comando automático encadeia coleta das auditorias, verificação das asserções e publicação dos resultados em uma única execução.
1014. [[lighthouseci-collect-targets]] — A coleta recebe uma lista de endereços, um diretório estático ou um comando que sobe o servidor, com padrão e prazo para considerar o serviço pronto.
1015. [[lighthouseci-number-of-runs]] — A configuração permite repetir a auditoria várias vezes por página e consolidar o resultado, geralmente pelo valor mediano.
1016. [[lighthouseci-assertions-presets]] — A verificação aceita um conjunto pré-definido de regras e permite desligar ou ajustar itens específicos, com nível de erro ou aviso.
1017. [[lighthouseci-numeric-assertions]] — Asserções podem fixar pontuação mínima ou valor máximo de métrica, com escolha do método de agregação entre as repetições.
1018. [[lighthouseci-performance-budgets]] — Um arquivo de orçamento declara limites de tamanho ou quantidade por tipo de recurso, e a auditoria correspondente pode ser verificada na esteira.
1019. [[lighthouseci-upload-targets]] — A publicação pode enviar ao armazenamento temporário público, gravar em diretório local ou integrar servidor próprio com histórico.
1020. [[lighthouseci-config-file]] — A configuração pode ficar em arquivo JavaScript, JSON ou YAML, com seções para coleta, verificação, publicação, servidor e assistente.
1021. [[lighthouseci-artifacts-and-reports]] — A coleta grava relatórios e um manifesto no diretório de resultados, e há comando para abrir as páginas geradas localmente.
1022. [[lighthouseci-limits-in-ci]] — Métricas de laboratório sofrem influência do executor, e diferenças pequenas entre revisões podem não corresponder a mudança de código.

### Pa11y — varredura de acessibilidade, padrões, ações e limites de automação

1023. [[pa11y-cli-basics]] — O comando recebe um endereço, abre a página em navegador sem interface e aplica verificações do motor escolhido, reportando os problemas encontrados.
1024. [[pa11y-standards-and-levels]] — O nível de conformidade pode ser declarado entre os três níveis de acessibilidade e é usado apenas pelo motor baseado em regras estáticas.
1025. [[pa11y-runners]] — A ferramenta aceita dois motores distintos de análise, e cada um mantém conjunto próprio de regras e forma de reportar resultados.
1026. [[pa11y-actions]] — Uma lista de ações executada antes da análise permite preencher campos, acionar botões e esperar mudanças de endereço, alcançando estados que exigem interação.
1027. [[pa11y-reporters-and-exit]] — A ferramenta oferece relatórios em texto, formato estruturado e formato de valores separados, e o código de saída indica se o limite de problemas foi excedido.
1028. [[pa11y-threshold-policy]] — Um limite numérico permite que a execução passe com quantidade pequena de problemas, controlado por parâmetro ou configuração.
1029. [[pa11y-ignore-and-scope]] — Regras específicas podem ser ignoradas, e a análise pode ser limitada a um elemento raiz ou excluir trechos selecionados da página.
1030. [[pa11y-config-file]] — As opções podem ser reunidas em arquivo de configuração, o que mantém a linha de comando curta e documenta o comportamento esperado.
1031. [[pa11y-ci-multiple-urls]] — A ferramenta complementar lê uma lista de endereços em arquivo de configuração ou os descobre por mapa do site e produz resumo conjunto da varredura.
1032. [[pa11y-ci-environment]] — A configuração pode declarar argumentos de lançamento do navegador, tempo limite e espera inicial, além de ajustes necessários em contêineres.
1033. [[pa11y-automation-limits]] — A varredura detecta parte dos problemas de acessibilidade, mas não avalia qualidade da experiência com tecnologia assistiva real.

### Prism — simulação e validação de contratos HTTP a partir de especificação

1034. [[prism-mock-mode]] — O comando de simulação lê um documento de contrato e expõe rotas que respondem conforme os exemplos ou os esquemas descritos nele.
1035. [[prism-static-vs-dynamic]] — O modo predefinido responde com os exemplos declarados no contrato, enquanto o modo dinâmico gera valores a partir dos esquemas.
1036. [[prism-prefer-header]] — O cabeçalho de preferência permite escolher código de resposta, exemplo específico e modo de geração para uma requisição simulada.
1037. [[prism-validation-errors]] — Na função de proxy, requisições que não respeitam o contrato são reportadas e podem ser rejeitadas com resposta de erro estruturada.
1038. [[prism-proxy-mode]] — O modo de intermediação encaminha requisições ao serviço real e pode comparar o tráfego com a especificação, mantendo o trânsito inalterado quando não há modo estrito.
1039. [[prism-generated-errors]] — Quando a requisição não corresponde ao contrato, a ferramenta responde com documento de problema estruturado e cabeçalho descrevendo a violação.
1040. [[prism-spec-quality]] — Rotas, parâmetros e respostas simuladas derivam diretamente do documento, e imprecisões aparecem como comportamento inesperado do servidor.
1041. [[prism-cli-workflow]] — A ferramenta de linha de comando oferece execução do servidor de simulação e do intermediário, com opções de porta, modo estrito e hospedagem do documento a partir de endereço remoto.
1042. [[prism-client-programmatic]] — A biblioteca permite criar instância de simulação a partir de operações específicas do contrato, com opções de geração dinâmica, validação e erro.
1043. [[prism-contract-first-workflow]] — A simulação só é útil quando o contrato é a fonte acordada entre quem consome e quem fornece, mantido antes da implementação.
1044. [[prism-limits]] — A ferramenta reproduz respostas previstas no contrato, sem manter estado entre chamadas nem aplicar regras de negócio.

### Hurl — arquivos de requisição, capturas, asserções e execução em lote

1045. [[hurl-file-structure]] — O arquivo descreve uma entrada com a requisição e, opcionalmente, a resposta esperada logo abaixo, incluindo código de status e cabeçalhos.
1046. [[hurl-implicit-assertions]] — Cabeçalhos declarados na resposta esperada são verificados automaticamente, sem necessidade de bloco explícito de asserções.
1047. [[hurl-captures]] — O bloco de capturas extrai valores da resposta por expressão e os disponibiliza como variáveis para as entradas seguintes do arquivo.
1048. [[hurl-assertions]] — O bloco de asserções aceita consultas ao corpo estruturado, contagens, comparações textuais e verificação de existência de cabeçalhos.
1049. [[hurl-status-and-error-handling]] — A execução considera falha quando a resposta diverge do esperado, e o código de saída indica se houve erro de asserção, de execução ou de configuração.
1050. [[hurl-options-block]] — O bloco de opções permite declarar por entrada ajustes como repetição com intervalo, atraso entre requisições e política de continuidade após erro.
1051. [[hurl-cli-test-mode]] — O modo de teste recebe arquivos ou diretórios, executa em paralelo com número controlado de tarefas e apresenta resumo por arquivo.
1052. [[hurl-session-scope]] — As entradas de um mesmo arquivo compartilham sessão, o que mantém cookies e variáveis entre requisições, enquanto arquivos distintos não compartilham.
1053. [[hurl-variables-and-reports]] — Variáveis podem ser definidas por linha de comando ou arquivo, e a execução gera relatórios em formatos de página e de resultado de testes.
1054. [[hurl-ci-integration]] — O código de saída e os relatórios permitem integrar a verificação de contrato a um pipeline, com recapitulação legível e resultado consumível por máquina.
1055. [[hurl-contract-verification-limits]] — Os arquivos verificam forma e valores das respostas que o serviço realmente devolve, sem validar a especificação nem substituir testes de comportamento.

## Tranche 17 — automação de navegador e dispositivos, simulação HTTP e contratos

### Gatling — simulações, injeção de carga, checagens e asserções

1056. [[gatling-simulation-structure]] — A simulação é uma classe executável que reúne o protocolo, os cenários e o perfil de injeção, permitindo versionar o teste de carga junto do serviço.
1057. [[gatling-scenario-flow]] — O cenário encadeia requisições, pausas e extrações de valores, representando o comportamento de um usuário virtual ao longo de uma sessão.
1058. [[gatling-injection-profiles]] — Os perfis definem como usuários virtuais entram ao longo do tempo, seja em modelo aberto pela taxa de chegada, seja em modelo fechado por usuários simultâneos.
1059. [[gatling-checks]] — As checagens avaliam cada resposta, como o código de status ou um campo do corpo, e registram falhas contabilizadas no relatório.
1060. [[gatling-session-and-extraction]] — Valores extraídos das respostas ficam guardados na sessão do usuário virtual e podem alimentar requisições posteriores do mesmo cenário.
1061. [[gatling-feeders]] — Os alimentadores fornecem valores a cada iteração, a partir de arquivos, bancos ou código, com estratégias de distribuição entre usuários virtuais.
1062. [[gatling-pauses-and-pacing]] — As pausas inserem intervalos entre ações, e a função de ritmo ajusta a espera para manter uma frequência estável de transações por usuário.
1063. [[gatling-assertions]] — As asserções comparam estatísticas globais ou por requisição com limites declarados e fazem a execução terminar com erro quando o critério não é atendido.
1064. [[gatling-http-protocol]] — O construtor de protocolo reúne endereço base, cabeçalhos, versão do protocolo e política de conexões aplicados a todos os cenários da simulação.
1065. [[gatling-reports-and-ci]] — Ao final da execução a ferramenta publica relatório navegável com séries temporais, distribuição de latências e contagem de falhas por requisição.

### Locust — usuários, tarefas, tempos de espera e formas de carga

1066. [[locust-locustfile-structure]] — O arquivo descreve classes de usuário com tarefas anotadas, e a ferramenta gera a carga executando essas tarefas em processos distribuídos.
1067. [[locust-tasks-and-weights]] — Cada tarefa recebe um peso que determina sua frequência relativa, permitindo representar a mistura de comportamentos observada no uso.
1068. [[locust-wait-time]] — O tempo de espera pode ser sorteado em uma faixa, constante ou calculado para manter um ritmo fixo de tarefas por usuário.
1069. [[locust-custom-load-shape]] — Uma classe de forma de carga decide, a cada intervalo, quantos usuários manter e a que velocidade criá-los, permitindo sequências de patamares.
1070. [[locust-user-lifecycle]] — Ganchos de início e término permitem autenticar o usuário virtual antes das tarefas e liberar recursos quando ele deixa a execução.
1071. [[locust-response-validation]] — O cliente permite capturar a resposta e declarar sucesso ou falha, cobrindo casos em que o código de status não expressa o resultado da operação.
1072. [[locust-tags-and-selection]] — Tarefas podem receber etiquetas e a execução pode incluir ou excluir etiquetas específicas, permitindo reaproveitar o mesmo arquivo em cenários diferentes.
1073. [[locust-distributed-execution]] — A execução pode dividir usuários entre vários processos trabalhadores coordenados por um processo principal, ampliando a capacidade de gerar carga.
1074. [[locust-headless-and-ci]] — A execução sem interface aceita número de usuários, velocidade de criação e tempo, grava resumos em arquivos e permite integrar a carga ao pipeline.
1075. [[locust-limits-and-interpretation]] — O resumo apresenta latências por percentil, taxa de requisições e falhas, mas descreve apenas o ponto de vista do cliente simulado.

### Robot Framework — palavras-chave, dados de teste, etiquetas e execução

1076. [[robot-test-case-syntax]] — Os testes são escritos em tabelas de seções, com o nome do caso seguido de chamadas de palavra-chave e seus argumentos.
1077. [[robot-keywords-and-arguments]] — Palavras-chave definidas pelo time agrupam passos repetidos, aceitam argumentos com valores padrão e podem devolver valores para o caso que as chama.
1078. [[robot-templates-data-driven]] — A configuração de modelo faz o caso executar a mesma palavra-chave para cada linha de dados, transformando a tabela em conjunto de cenários.
1079. [[robot-setup-teardown]] — Configurações e limpezas podem ser declaradas para a suíte, cada caso ou cada palavra-chave, com ordem de execução definida entre os níveis.
1080. [[robot-tags-and-selection]] — Etiquetas classificam casos e suítes e podem ser usadas na linha de comando para incluir, excluir ou exigir combinações.
1081. [[robot-teardown-and-continuation]] — Palavras-chave de verificação e o comportamento de continuidade permitem executar todas as verificações de um caso mesmo quando uma delas falha.
1082. [[robot-variables-and-scopes]] — Variáveis podem ser locais ao caso, comuns à suíte, globais à execução ou passadas por linha de comando, com precedência definida entre elas.
1083. [[robot-timeouts-and-stability]] — É possível declarar tempo limite por caso ou por suíte e usar palavras-chave de espera que aguardam condições observáveis em vez de pausas fixas.
1084. [[robot-libraries-and-extensions]] — O framework traz bibliotecas padrão e aceita bibliotecas próprias ou de terceiros, cujas palavras-chave passam a integrar o vocabulário dos testes.
1085. [[robot-reports-and-ci]] — Cada execução gera arquivos de registro e relatório, e a ferramenta de reprocessamento permite combinar resultados parciais e mudar o formato da saída.

### Cucumber — Gherkin, definições de passo, ganchos e execução paralela

1086. [[cucumber-gherkin-structure]] — O arquivo de funcionalidade descreve cenários com passos iniciados por palavras reservadas e um contexto curto no topo da funcionalidade.
1087. [[cucumber-step-definitions]] — Cada passo do cenário corresponde a uma definição de passo que reconhece o texto, extrai parâmetros e executa a ação sobre o sistema.
1088. [[cucumber-scenario-outline-examples]] — O esquema de cenário usa marcadores no texto e uma tabela de exemplos, gerando uma execução por linha e um relatório por combinação.
1089. [[cucumber-hooks-lifecycle]] — Ganchos executados antes e depois de cenários, passos ou da execução permitem preparar estado e liberar recursos em pontos controlados.
1090. [[cucumber-tags-and-expressions]] — Etiquetas aplicadas a funcionalidades, cenários e exemplos podem ser combinadas em expressões lógicas para selecionar o que será executado.
1091. [[cucumber-background-and-data-tables]] — O antecedente repete um contexto no início de cada cenário da funcionalidade, e tabelas nos passos organizam dados estruturados de forma legível.
1092. [[cucumber-parallel-execution]] — A execução pode distribuir cenários entre processos, respeitando limites de paralelismo e mantendo relatórios individuais por processo.
1093. [[cucumber-reports]] — A execução pode gerar relatórios legíveis, arquivos estruturados e saídas consumíveis por servidores de integração, a partir do mesmo resultado.
1094. [[cucumber-living-documentation]] — Como os cenários são executáveis, eles permanecem verdadeiros enquanto a suíte passa, servindo de documentação do comportamento acordado.
1095. [[cucumber-limits-and-maintenance]] — A camada de cenários precisa de manutenção, com passos reutilizáveis, dados controlados e decisão explícita sobre o que pertence a ela.

### Selenium WebDriver — localizadores, esperas, objetos de página e grade

1096. [[selenium-locator-strategy]] — Os localizadores identificam elementos por identificador, seletor de estilo, texto visível ou caminho estrutural, com estabilidade decrescente nessa ordem em geral.
1097. [[selenium-explicit-waits]] — A espera explícita repete uma condição até que ela seja satisfeita ou o tempo limite se esgote, aceitando exceções ignoradas durante a verificação.
1098. [[selenium-page-objects]] — Um objeto de página expõe serviços da tela por métodos, escondendo localizadores e devolvendo outros objetos de página ou valores de negócio.
1099. [[selenium-actions-api]] — A interface de ações permite encadear movimento do ponteiro, cliques, arrasto, digitação e combinações de teclas, liberando o conjunto de uma vez.
1100. [[selenium-frames-windows-alerts]] — O driver permite entrar em quadros, mudar de janela e tratar caixas de diálogo, sempre com troca explícita de contexto antes de interagir.
1101. [[selenium-grid-distributed]] — A grade recebe sessões, escolhe um nó compatível com as capacidades pedidas e devolve o endereço da sessão para o cliente.
1102. [[selenium-browser-options]] — Cada navegador aceita opções de inicialização, como modo sem interface, argumentos de segurança, tamanho de janela e preferências de download.
1103. [[selenium-screenshot-and-evidence]] — O driver permite capturar imagens da tela, e a captura costuma ser associada a ganchos que gravam artefato apenas quando o teste falha.
1104. [[selenium-flakiness-diagnosis]] — Falhas intermitentes costumam vir de esperas mal colocadas, dados compartilhados, animações ou dependências externas lentas, e não do driver.
1105. [[selenium-limits-and-practices]] — O driver automatiza o navegador, mas não valida conteúdo, desempenho nem acessibilidade, e a suíte precisa ser combinada com outras verificações.

### Appium — capacidades, drivers, seletores e sessões móveis paralelas

1106. [[appium-capabilities]] — As capacidades descrevem plataforma, automação, dispositivo e aplicativo, definindo o que a sessão vai controlar antes de qualquer comando.
1107. [[appium-drivers-architecture]] — O servidor é extensível, e cada plataforma é suportada por um driver instalado separadamente, com a automação escolhida por capacidade.
1108. [[appium-locator-strategies]] — Os seletores variam por plataforma, incluindo identificador de acessibilidade, atributos nativos e estratégias específicas de cada automação.
1109. [[appium-mobile-gestures]] — A sessão expõe comandos para deslizar, tocar em coordenadas, pressionar por tempo e executar ações encadeadas com o ponteiro.
1110. [[appium-hybrid-context]] — Aplicativos híbridos expõem contextos distintos, e a sessão precisa mudar para o contexto web antes de usar seletores de página.
1111. [[appium-session-reset]] — Opções de sessão definem se o aplicativo é reinstalado, se os dados são apagados e se o estado é preservado entre execuções.
1112. [[appium-parallel-sessions]] — O servidor pode manter várias sessões simultâneas, e cada uma precisa de porta de sistema e identificador de dispositivo próprios para não colidir.
1113. [[appium-inspector]] — A ferramenta de inspeção mostra a árvore de elementos de uma sessão ativa, permitindo descobrir identificadores e validar seletores antes de escrever o teste.
1114. [[appium-device-farm]] — A mesma sessão pode apontar para dispositivos físicos locais ou serviços de nuvem que expõem endereços compatíveis com o protocolo.
1115. [[appium-limits-and-practices]] — A automação móvel depende de sistema operacional, fabricante e permissões, e a suíte precisa ser pequena, estável e focada em fluxos críticos.

### WireMock — stubs, correspondência de requisições, cenários e verificação

1116. [[wiremock-stub-mapping]] — Um stub associa critérios de correspondência da requisição a uma resposta predefinida, em arquivo, código ou documento estruturado.
1117. [[wiremock-request-matching]] — Os critérios podem exigir caminho exato ou por padrão, método, cabeçalhos e condições sobre o corpo em formatos estruturados.
1118. [[wiremock-response-templating]] — A resposta pode usar modelos que leem valores da requisição, geram identificadores e formatam datas no momento da chamada.
1119. [[wiremock-stateful-scenarios]] — Um cenário é uma máquina de estados que começa em um estado inicial e muda conforme as chamadas, permitindo representar sequências.
1120. [[wiremock-priorities]] — Quando mais de um stub corresponde à mesma requisição, a prioridade decide qual deles responde, com padrão definido para os casos não declarados.
1121. [[wiremock-fault-simulation]] — O servidor pode responder com atraso fixo ou variável, encerrar conexões e devolver respostas malformadas para testar o tratamento de falhas do cliente.
1122. [[wiremock-verification]] — O servidor registra as requisições e permite verificar ocorrências por critérios, contando chamadas a uma rota específica.
1123. [[wiremock-record-playback]] — O servidor pode atuar como intermediário, capturar respostas de um serviço real e gerar stubs automaticamente a partir do tráfego observado.
1124. [[wiremock-standalone-and-ci]] — O servidor pode rodar como processo independente ou contêiner, aceitando diretório de stubs e porta por argumento de linha de comando.
1125. [[wiremock-limits-and-practices]] — O simulador reproduz respostas definidas, sem lógica de negócio, persistência real nem garantia de que o serviço verdadeiro se comporta assim.

### Pact — contratos entre consumidor e provedor, correspondência e broker

1126. [[pact-consumer-driven]] — O consumidor escreve expectativas sobre as requisições que faz e as respostas que espera, e esse registro vira um artefato verificável pelo provedor.
1127. [[pact-consumer-test-dsl]] — A interface de teste descreve o estado inicial, a requisição esperada e a resposta simulada, e executa o código do consumidor contra esse dublê.
1128. [[pact-matching-rules]] — As regras de correspondência verificam forma e tipo em vez de valores exatos, aceitando identificadores variáveis, listas de tamanho mínimo e padrões textuais.
1129. [[pact-provider-states]] — Cada interação pode declarar o estado em que o provedor deve estar, e o lado do provedor implementa a preparação correspondente àquele estado.
1130. [[pact-provider-verification]] — A ferramenta de verificação lê os contratos publicados, executa cada interação contra o serviço real e reporta o resultado por contrato.
1131. [[pact-publish-and-broker]] — Os arquivos de contrato gerados pelos testes do consumidor são publicados em um serviço central com versão e identificação do aplicativo.
1132. [[pact-can-i-deploy]] — A consulta de autorização verifica se a versão prestes a ser implantada tem todos os contratos e verificações compatíveis com o ambiente de destino.
1133. [[pact-versioning-and-selectors]] — Os seletores definem quais contratos o provedor verifica, combinando ramos, etiquetas, ambiente ou contratos em andamento.
1134. [[pact-webhooks-and-pending]] — Avisos automáticos podem disparar verificações quando um contrato muda, e contratos em andamento permitem que o provedor os teste sem bloquear o pipeline.
1135. [[pact-limits-and-practices]] — O contrato cobre a forma da interação acordada, mas não verifica regras de negócio, desempenho nem o comportamento completo do provedor.

### Testify — asserções, suítes, dublês e testes HTTP em Go

1136. [[testify-assert-vs-require]] — O pacote de asserção registra a falha e continua a execução, enquanto o pacote equivalente interrompe o teste no primeiro erro.
1137. [[testify-equality-assertions]] — As funções de comparação distinguem igualdade profunda, identidade de objeto e comparação de conteúdo, exibindo diferenças legíveis no relatório.
1138. [[testify-error-assertions]] — Há funções específicas para confirmar que uma chamada devolve erro, que o erro é de determinado tipo ou que corresponde a um erro conhecido.
1139. [[testify-suite-lifecycle]] — O pacote de suíte agrupa métodos de teste em uma estrutura, com preparação e limpeza por caso ou por conjunto, executadas na ordem definida.
1140. [[testify-mock-expectations]] — O pacote de dublês permite registrar chamadas esperadas com argumentos e valores de retorno e verificar, ao final, se todas ocorreram.
1141. [[testify-mock-argument-matchers]] — Os dublês aceitam funções de correspondência nos argumentos, permitindo casar por tipo ou por parte do valor em vez de exigir igualdade exata.
1142. [[testify-mock-generation]] — A geração automática produz implementações de dublê a partir das interfaces do projeto, mantendo o código de apoio sincronizado com as assinaturas.
1143. [[testify-http-testing]] — O suporte a HTTP auxilia a montar requisições e verificar respostas, embora os utilitários de servidor de teste da biblioteca padrão sejam hoje a recomendação.
1144. [[testifylint-and-consistency]] — Ferramentas de análise específicas apontam usos incorretos das asserções, como ordem trocada de esperado e obtido ou comparações que deveriam ser fatais.
1145. [[testify-limits-and-practices]] — A biblioteca melhora a legibilidade das asserções, mas não substitui o executor padrão nem decide quais comportamentos merecem verificação.

### RSpec — exemplos, expectativas, dublês, ganchos e exemplos compartilhados

1146. [[rspec-describe-and-context]] — Um grupo de exemplos descreve o comportamento de uma classe ou método, e contextos internos separam situações diferentes desse mesmo comportamento.
1147. [[rspec-expectations-matchers]] — As expectativas combinam um valor observado com um matcher, cobrindo igualdade, correspondência de padrão, mudança de estado e exceções.
1148. [[rspec-let-and-subject]] — Os auxiliares de definição criam valores avaliados no primeiro uso e memorizados por exemplo, e o sujeito nomeado descreve o objeto principal.
1149. [[rspec-hooks]] — Ganchos de antes, depois e ao redor envolvem os exemplos, com escopo por exemplo, por grupo ou na suíte, respeitando a ordem dos grupos.
1150. [[rspec-doubles-and-stubs]] — Dublês verificados imitam a interface real, e permissões de recebimento configuram respostas sem exigir que a chamada aconteça.
1151. [[rspec-message-expectations]] — Uma expectativa de mensagem configura o recebimento e falha o exemplo se a chamada não ocorrer, distinguindo-se da permissão simples.
1152. [[rspec-argument-matchers]] — Nas expectativas e permissões é possível casar argumentos por expressão, inclusão parcial e padrão, em vez de exigir igualdade exata.
1153. [[rspec-shared-examples]] — Blocos de exemplos compartilhados descrevem comportamento comum e são incluídos em grupos diferentes, com parâmetros e contexto próprio.
1154. [[rspec-metadata-and-filtering]] — Os grupos e exemplos aceitam metadados, e a configuração pode aplicar ganchos ou filtros conforme esses metadados.
1155. [[rspec-configuration-and-profiling]] — O arquivo de configuração define filtros, formato de saída, perfil de execução e ordem dos exemplos, e a execução pode apontar os exemplos mais lentos.
1156. [[rspec-limits-and-practices]] — A suíte verifica comportamento e colaboração, mas depende de disciplina para manter exemplos independentes e mensagens de falha úteis.

## Tranche 18 — acessibilidade, análise estática, segurança de artefatos e relatórios de teste

### Cypress — testes end-to-end no navegador, interceptação e sessões

1157. [[cypress-architecture-in-browser]] — O executor roda no mesmo ciclo do aplicativo, dentro do navegador, comunicando-se com um processo externo responsável por orquestrar a execução.
1158. [[cypress-retry-ability]] — Consultas e asserções são repetidas até que a condição se torne verdadeira ou o tempo limite se esgote, sem interromper a cadeia de comandos.
1159. [[cypress-interception]] — O comando de interceptação observa, substitui ou atrasa requisições, permitindo simular respostas e aguardar chamadas específicas por apelido.
1160. [[cypress-session-caching]] — O comando de sessão executa o fluxo de autenticação uma vez e restaura o estado em testes seguintes, com validação opcional dessa restauração.
1161. [[cypress-selectors-and-testids]] — As consultas aceitam seletores de estilo, atributos dedicados à automação e textos visíveis, com estabilidade diferente entre eles.
1162. [[cypress-fixtures]] — Os arquivos de apoio guardam dados de teste e podem alimentar respostas simuladas ou servir de origem para o estado inicial do cenário.
1163. [[cypress-custom-commands]] — É possível registrar comandos personalizados e sobrescrever comandos existentes, reunindo sequências repetidas em uma operação nomeada.
1164. [[cypress-timeouts-and-stability]] — Limites de tempo podem ser definidos por comando, por asserção ou para toda a configuração, e a espera por condição é preferível a pausas fixas.
1165. [[cypress-debugging-and-artifacts]] — A execução registra vídeos e capturas, permite consultar o log de comandos e o tráfego de rede, e oferece modo interativo para inspeção.
1166. [[cypress-ci-parallelization]] — A suíte pode ser dividida em várias máquinas e os resultados combinados, com balanceamento por tempo de execução ou por grupos declarados.

### WebdriverIO — seletores, esperas, serviços, comandos próprios e execução

1167. [[wdio-selectors]] — Os seletores aceitam estilo, texto, identificador de acessibilidade e estratégias específicas de plataforma móvel, com retorno de um ou vários elementos.
1168. [[wdio-waiting-strategies]] — Os elementos expõem esperas específicas para exibição, existência, clicabilidade e estado habilitado, com limite de tempo configurável.
1169. [[wdio-sync-and-async]] — O framework oferece modo síncrono que oculta as promessas e modo assíncrono explícito, com regras distintas de configuração.
1170. [[wdio-element-commands]] — Os elementos oferecem comandos para interagir, consultar estado e atributos, e as ações podem ser encadeadas na mesma chamada.
1171. [[wdio-services]] — Os serviços preparam e encerram componentes externos, como servidor de navegador, emulador ou servidor de aplicação, integrados ao ciclo da suíte.
1172. [[wdio-custom-commands]] — Comandos personalizados podem ser adicionados ao navegador ou aos elementos, encapsulando sequências usadas em vários testes.
1173. [[wdio-configuration]] — O arquivo de configuração declara navegadores, capacidades, estrutura de testes, relatórios, serviços e opções de execução.
1174. [[wdio-reporters-and-artifacts]] — A suíte pode gerar relatórios em formatos diferentes, incluir capturas em falhas e publicar resultados para consumo no pipeline.
1175. [[wdio-parallel-execution]] — A configuração permite distribuir arquivos de teste entre instâncias de navegador, com limite de processos simultâneos definido por capacidade.
1176. [[wdio-mobile-and-multiremote]] — As mesmas capacidades atendem navegador e dispositivos móveis, e o modo multirremoto permite controlar várias sessões na mesma execução.

### JUnit 5 — ciclos de vida, parametrização, extensões e execução paralela

1177. [[junit5-annotations-basics]] — As anotações identificam métodos e classes de teste, com variantes para desabilitar, exibir nome personalizado e ordenar a execução.
1178. [[junit5-lifecycle]] — As anotações de ciclo de vida permitem preparar por método, por classe ou por execução, com controle de herança e de ordem entre extensões.
1179. [[junit5-assertions]] — O conjunto de asserções cobre igualdade, agrupamento de verificações, exceções esperadas e limites de tempo, com mensagem de falha personalizável.
1180. [[junit5-parameterized]] — Os testes parametrizados recebem argumentos de fontes declaradas, com formatos de exibição que identificam cada invocação no relatório.
1181. [[junit5-dynamic-tests]] — Métodos de fábrica podem produzir casos dinamicamente, com nome e conteúdo definidos a partir de dados disponíveis apenas durante a execução.
1182. [[junit5-extensions]] — As extensões podem interceptar fases do ciclo de vida e resolver parâmetros, sendo registradas por anotação, por anotação composta ou por configuração global.
1183. [[junit5-dependency-injection]] — Construtores e métodos de teste podem receber parâmetros resolvidos por extensões registradas, incluindo informações do teste corrente e recursos preparados.
1184. [[junit5-parallel-execution]] — A execução paralela é opcional e configurada por parâmetros que definem modo padrão, modo por classe e estratégia de paralelismo.
1185. [[junit5-tagging-and-filtering]] — As etiquetas classificam testes e podem ser usadas para incluir ou excluir grupos na execução, inclusive por configuração de construção.
1186. [[junit5-migration-and-practices]] — A versão atual convive com a anterior por meio de mecanismo de compatibilidade, permitindo migração gradual de classes e asserções.

### GoogleTest — asserções, fixtures, parametrização e relatórios em C++

1187. [[googletest-test-macros]] — As macros declaram casos de teste com nome de suíte e nome do caso, gerando a função de entrada e o registro automático no executor.
1188. [[googletest-assertions]] — As asserções fatais interrompem o caso no primeiro erro, enquanto as não fatais registram a falha e continuam a execução.
1189. [[googletest-comparisons]] — As macros de comparação cobrem igualdade, desigualdade, comparações numéricas, texto e valores de ponto flutuante com tolerância declarada.
1190. [[googletest-fixtures]] — Uma classe de fixture herda da classe base de teste e define preparação e limpeza, que são executadas para cada caso que usa a fixture.
1191. [[googletest-parameterized]] — O gerador de valores combinado com a macro de teste parametrizado cria um caso por valor, com nome derivado e relatório individual.
1192. [[googletest-typed-tests]] — Os testes por tipo permitem executar a mesma bateria sobre várias implementações que compartilham interface, e a suíte é instanciada para cada tipo.
1193. [[googletest-mocks-integration]] — A biblioteca de dublês complementa o framework, declarando expectativas sobre chamadas e valores de retorno das dependências.
1194. [[googletest-death-tests]] — As asserções de morte verificam que determinado trecho encerra o processo, opcionalmente conferindo o código de saída e a mensagem emitida.
1195. [[googletest-running-and-filtering]] — O executável aceita filtros por nome de suíte e de caso, repetição, ordem aleatória e saída em formatos consumíveis por ferramentas.
1196. [[googletest-reports-and-limits]] — A saída lista falhas com arquivo e linha, permite formatos estruturados e pode ser combinada com outras ferramentas de execução.

### PHPUnit — asserções, provedores de dados, dublês e cobertura

1197. [[phpunit-test-structure]] — Cada classe de teste herda da classe base do framework, e os métodos de teste são declarados publicamente segundo a convenção de nome.
1198. [[phpunit-assertions]] — O conjunto cobre igualdade estrita, identidade de objeto, comparações numéricas, expressões regulares, exceções e estado de coleções.
1199. [[phpunit-data-providers]] — Os provedores fornecem conjuntos de argumentos, e cada conjunto aparece como teste separado no relatório quando identificado por nome.
1200. [[phpunit-fixtures]] — Os métodos de preparação e limpeza são executados antes e depois de cada teste, e há variantes no nível da classe para recursos compartilhados.
1201. [[phpunit-test-doubles]] — O framework cria dublês de tipos, com configuração de retornos, exceções e verificação de chamadas, além de restringir a geração automática de valores.
1202. [[phpunit-coverage]] — Com a extensão apropriada habilitada, a execução coleta dados de linhas e ramos e permite gerar relatórios em formatos distintos.
1203. [[phpunit-exception-testing]] — As asserções de exceção confirmam a classe lançada e permitem inspecionar a mensagem, com cuidados sobre o trecho realmente coberto pela verificação.
1204. [[phpunit-groups-and-filtering]] — Grupos e filtros permitem incluir ou excluir conjuntos de testes, e a configuração do projeto pode declarar suítes separadas por tipo.
1205. [[phpunit-ci-and-reports]] — A execução gera relatórios em formatos consumíveis por ferramentas de integração, com detalhe por teste e resumo de falhas.
1206. [[phpunit-limits-and-practices]] — O framework verifica unidades e integrações, mas a qualidade da suíte depende de casos independentes e verificações significativas.

### Ginkgo — especificações em Go, ciclo de vida, paralelismo e etiquetas

1207. [[ginkgo-container-nodes]] — Contêineres aninhados de descrição, contexto e condição agrupam especificações e comunicam a hierarquia de cenários.
1208. [[ginkgo-setup-nodes]] — Nós de preparação são executados antes e depois de cada especificação, com variantes de suíte e de contêiner ordenado.
1209. [[ginkgo-subject-and-assertions]] — As especificações contêm as verificações, normalmente com a biblioteca de asserções complementar, e o relatório destaca a primeira falha.
1210. [[ginkgo-parallel-execution]] — A ferramenta de linha de comando distribui especificações entre processos, e cada processo executa uma cópia do binário de teste.
1211. [[ginkgo-ordered-and-serial]] — Contêineres podem ser marcados como ordenados, e especificações ou contêineres podem ser declarados seriais para nunca rodarem simultaneamente.
1212. [[ginkgo-labels-and-filtering]] — Etiquetas aplicadas a especificações e contêineres podem ser combinadas em expressões para filtrar a execução por linha de comando.
1213. [[ginkgo-suite-bootstrap]] — O ponto de entrada cria o executor, prepara e limpa recursos da suíte e entrega o controle ao framework para executar as especificações.
1214. [[ginkgo-reporting-and-artifacts]] — A suíte produz relatórios com hierarquia de contêineres, permite saída consumível por máquina e grava arquivos de perfil para depuração.
1215. [[ginkgo-focus-and-pending]] — É possível marcar especificações como focadas, pendentes de implementação ou ignoradas temporariamente, com aviso sobre o uso de foco.
1216. [[ginkgo-cli-and-limits]] — A ferramenta de linha de comando gera, executa, filtra e perfila suítes, inclusive em modo de observação contínua durante o desenvolvimento.

### axe-core — regras de acessibilidade, impacto e integração automatizada

1217. [[axe-run-and-results]] — A chamada de análise recebe contexto e opções e devolve violações, itens aprovados, avisos e regras não aplicáveis.
1218. [[axe-rule-tags]] — Cada regra possui etiquetas que indicam nível de conformidade e critério relacionado, e a análise pode ser restringida a elas.
1219. [[axe-impact-levels]] — Cada violação traz um nível de impacto, e cada elemento afetado inclui seletor, trecho de marcação e resumo da falha.
1220. [[axe-configuration-and-exclusions]] — As opções permitem habilitar ou desabilitar regras específicas e limitar a análise a regiões da página.
1221. [[axe-experimental-rules]] — Regras marcadas como experimentais não rodam por padrão e precisam ser nomeadas explicitamente para entrar na análise.
1222. [[axe-browser-integration]] — O pacote de integração injeta a biblioteca na página e executa a análise durante o teste de interface, com limite de tempo e opções.
1223. [[axe-ci-policy]] — A execução pode falhar conforme a política escolhida, seja por qualquer violação, por níveis de impacto ou por lista de regras.
1224. [[axe-manual-complement]] — A análise automática cobre parte dos critérios e não avalia experiência real com tecnologia assistiva nem ordem de foco percebida.
1225. [[axe-baseline-and-history]] — Registrar a contagem por regra e por versão do código permite medir a evolução do passivo e comparar execuções.
1226. [[axe-common-violations]] — As regras mais acionadas costumam envolver texto alternativo, rótulos de formulário, contraste, estrutura de cabeçalhos e identificação de idioma.
1227. [[axe-limits]] — A biblioteca detecta uma parte dos problemas de acessibilidade e não substitui avaliação com pessoas usuárias nem revisão de conteúdo.

### Semgrep — regras de análise estática, padrões, correções e pipeline

1228. [[semgrep-rule-structure]] — Uma regra declara identificador, linguagem, severidade, mensagem e o padrão que deve corresponder ao código analisado.
1229. [[semgrep-pattern-operators]] — Operadores permitem exigir várias condições, alternativas, negação, contexto interno e correspondência por expressão regular sobre metavariáveis.
1230. [[semgrep-metavariables]] — As metavariáveis representam trechos variáveis do código e podem ser reutilizadas para exigir que duas posições correspondam ao mesmo valor.
1231. [[semgrep-taint-mode]] — O modo de propagação descreve fontes, destinos e saneadores, acompanhando a passagem de dados não confiáveis até operações sensíveis.
1232. [[semgrep-rule-defined-fix]] — Regras podem declarar a substituição apropriada, e a ferramenta aplica a correção diretamente ou mostra a prévia para revisão.
1233. [[semgrep-ci-integration]] — A execução pode analisar o repositório inteiro ou apenas as mudanças, gerar saída estruturada e falhar o trabalho pela presença de achados.
1234. [[semgrep-suppressions]] — Achados podem ser silenciados com anotação no código, e a supressão pode ser restrita ao escopo onde o risco é aceito.
1235. [[semgrep-severity-and-policy]] — As regras declaram severidade, e a execução pode falhar por severidade mínima ou por regra específica conforme a política do projeto.
1236. [[semgrep-custom-rules]] — Regras locais ficam versionadas com o código e podem cobrir convenções internas que ferramentas genéricas não conhecem.
1237. [[semgrep-limits-and-practices]] — A análise identifica padrões e fluxos modelados, mas não substitui execução, revisão de projeto nem testes de comportamento.

### Trivy — varredura de imagens, configurações, segredos e inventário

1238. [[trivy-targets-and-scanners]] — A ferramenta distingue o que é analisado, como imagem, sistema de arquivos ou configuração, do que é procurado, como vulnerabilidades, segredos ou falhas de configuração.
1239. [[trivy-image-scanning]] — A imagem é analisada camada a camada, cruzando os pacotes instalados com bases de vulnerabilidades e filtrando por gravidade.
1240. [[trivy-filesystem-and-repo]] — A varredura pode percorrer diretório local ou repositório remoto, encontrando dependências declaradas, segredos e configurações no código.
1241. [[trivy-misconfiguration]] — O verificador de configuração avalia arquivos de infraestrutura como definições de contêiner, manifestos de orquestração e modelos de provisionamento.
1242. [[trivy-secret-scanning]] — O verificador de segredos procura credenciais, chaves e tokens em arquivos e camadas, com regras próprias e possibilidade de exceções.
1243. [[trivy-sbom]] — A ferramenta produz inventário em formatos padronizados a partir de imagens e sistemas de arquivos, e também analisa inventários existentes.
1244. [[trivy-ignore-and-baseline]] — Achados podem ser ignorados por arquivo de configuração com identificadores e, quando suportado, prazo de expiração e justificativa.
1245. [[trivy-ci-policy]] — A execução pode falhar por código de saída a partir de gravidade mínima ou de achados encontrados, com filtros de severidade e de correção disponível.
1246. [[trivy-formats-and-output]] — A ferramenta gera saída em tabela para leitura e em formatos estruturados, inclusive padronizados para intercâmbio com outras ferramentas.
1247. [[trivy-limits-and-practices]] — A ferramenta encontra componentes conhecidos e padrões de configuração, mas não substitui análise de falhas de lógica nem testes de invasão.

### Allure — relatórios, passos, anexos, categorias e histórico

1248. [[allure-results-and-report]] — A execução dos testes grava arquivos de resultado em diretório próprio, e o gerador transforma esse conjunto em relatório navegável estático.
1249. [[allure-steps]] — Anotações de passo dividem o teste em ações nomeadas, com possibilidade de aninhamento e parametrização do nome exibido.
1250. [[allure-attachments]] — Arquivos podem ser anexados ao teste ou a um passo específico, com tipo declarado, incluindo texto, imagem e conteúdo estruturado.
1251. [[allure-categories]] — O arquivo de configuração define categorias por status e por expressões sobre mensagem e rastro, agrupando falhas segundo a origem provável.
1252. [[allure-severity-and-annotations]] — Anotações registram gravidade, descrição, vínculo com requisito e agrupamento por épico, funcionalidade e história.
1253. [[allure-history-and-trends]] — Ao manter relatórios anteriores acessíveis, o gerador calcula tendências de resultado e duração entre execuções.
1254. [[allure-retries-and-flaky]] — O relatório mostra tentativas do mesmo caso, distinguindo o resultado final do histórico de execuções intermediárias.
1255. [[allure-suites-and-behaviors]] — O relatório organiza os casos por estrutura de execução, por pacotes e por agrupamento de comportamento declarado nas anotações.
1256. [[allure-ci-publication]] — O gerador produz página estática que pode ser publicada como artefato do trabalho ou em serviço de hospedagem de relatórios.
1257. [[allure-limits-and-practices]] — O relatório apresenta o que a execução registrou, sem julgar a qualidade das verificações nem substituir a análise das causas.

## Tranche 19 — frameworks de sistema, virtualização de serviços, nuvem local, infraestrutura e análise de arquitetura

### Catch2 — casos de teste, seções, asserções, geradores e relatórios em C++

1258. [[catch2-test-case-basics]] — Casos de teste são declarados com macros que os registram automaticamente e recebem nome livre e etiquetas entre colchetes.
1259. [[catch2-assertions]] — A biblioteca oferece macros que interrompem o caso ao falhar e macros que registram a falha e continuam a execução.
1260. [[catch2-sections]] — Seções descrevem caminhos dentro do mesmo caso, e cada seção é executada com o estado inicial restaurado.
1261. [[catch2-test-fixtures]] — Fixtures são classes com preparação e limpeza opcionais, usadas quando seções não bastam para o estado comum.
1262. [[catch2-generators]] — Geradores percorrem valores em sequência dentro do caso, e geradores no mesmo escopo produzem o produto cartesiano das entradas.
1263. [[catch2-matchers]] — Matchers compõem verificações sobre propriedades de valores, incluindo conteúdo, faixa, comparação aproximada e predicados próprios.
1264. [[catch2-floating-point]] — O framework fornece comparação com tolerância relativa ou absoluta para valores de ponto flutuante e classes aproximadas.
1265. [[catch2-reporters]] — A execução aceita múltiplos relatórios simultâneos, com saída legível para pessoas e formatos estruturados para integração.
1266. [[catch2-command-line]] — A linha de comando permite filtrar por nome e etiqueta, listar casos, embaralhar a ordem e repetir a execução fixando a semente.
1267. [[catch2-integration-limits]] — A biblioteca se integra a sistemas de construção, permite descobrir casos para registro automático e cobre verificação unitária e de componentes.

### TestCafe — fixtures, seletores, ações, asserções e papéis no navegador

1268. [[testcafe-fixtures-and-tests]] — Cada arquivo declara uma fixture com a página inicial e agrupa casos de teste que compartilham configuração e ganchos.
1269. [[testcafe-selectors]] — Seletores consultam o DOM de forma assíncrona e aceitam filtros por texto, atributo, índice e relação entre elementos.
1270. [[testcafe-assertions]] — As asserções aguardam a condição até o limite configurado antes de falhar, cobrindo igualdade, conteúdo, expressão regular e negações.
1271. [[testcafe-actions]] — Ações do controlador cobrem clique, digitação, teclas, arrasto, navegação e requisição, e podem ser encadeadas quando não retornam valor.
1272. [[testcafe-roles]] — Papéis definem uma sequência de entrada uma única vez e podem ser ativados em vários casos, reutilizando a sessão autenticada.
1273. [[testcafe-client-functions]] — Funções de cliente permitem ler e alterar estado do navegador, como armazenamento local, endereço e APIs expostas pela página.
1274. [[testcafe-request-hooks]] — Ganchos de requisição permitem observar, simular e substituir chamadas de rede, incluindo atrasos e códigos de erro.
1275. [[testcafe-parallelism-and-browsers]] — A execução aceita múltiplos navegadores, inclusive remotos, e distribui casos em processos paralelos com controle de concorrência.
1276. [[testcafe-debugging-and-artifacts]] — A ferramenta oferece modo de depuração com pausa no navegador, captura de tela em falhas e relatórios configuráveis.
1277. [[testcafe-limits-and-practices]] — A ferramenta executa testes de interface sem driver externo, injetando o controlador na página durante a execução.

### Mountebank — impostores, stubs, predicados, proxies e comportamento

1278. [[mountebank-imposters]] — Um impostor é um serviço virtual que escuta em uma porta e fala um protocolo, definido por porta, protocolo e lista de stubs.
1279. [[mountebank-stubs]] — Cada stub reúne predicados opcionais e uma lista de respostas, e a primeira resposta é devolvida a cada correspondência.
1280. [[mountebank-predicates]] — Predicados comparam método, caminho, cabeçalhos, consulta e corpo com operadores de igualdade, padrão, existência e negação.
1281. [[mountebank-proxies]] — Uma resposta em modo proxy encaminha a requisição ao serviço real e pode registrar a resposta para reprodução posterior.
1282. [[mountebank-behaviors]] — Comportamentos modificam a resposta, adicionando atraso, substituindo conteúdo por dados da requisição e repetindo respostas sem avançar a sequência.
1283. [[mountebank-injection]] — A injeção executa função em JavaScript para decidir o predicado ou montar a resposta, com acesso à requisição recebida.
1284. [[mountebank-recorded-requests]] — Com o registro ativado, o impostor guarda as requisições recebidas e as disponibiliza para consulta posterior.
1285. [[mountebank-file-based-setup]] — A configuração pode ser descrita em arquivo carregado na inicialização, permitindo versionar os serviços virtuais com o projeto.
1286. [[mountebank-ci-integration]] — O serviço pode subir como processo ou contêiner na esteira, e os impostores são criados por configuração antes dos testes.
1287. [[mountebank-limits-and-practices]] — Simular serviços permite verificar o cliente contra respostas controladas, mas não valida o contrato real nem o comportamento do provedor.

### LocalStack — emulação de serviços de nuvem, ganchos de inicialização e testes

1288. [[localstack-service-emulation]] — O LocalStack expõe uma porta de entrada que atende chamadas de diversos serviços de nuvem em ambiente local, com credenciais fictícias.
1289. [[localstack-init-hooks]] — Scripts em diretórios de fases distintas são executados na subida, quando o serviço fica pronto e no encerramento do contêiner.
1290. [[localstack-init-troubleshooting]] — A ausência de execução costuma vir de caminho incorreto, permissão de arquivo, ordem alfabética ou serviço indisponível no momento do script.
1291. [[localstack-docker-compose]] — A composição declara o serviço, a porta de entrada, as variáveis de ambiente e os volumes que trazem os ganchos e o estado persistente.
1292. [[localstack-persistence]] — A pasta montada preserva recursos entre reinícios quando a persistência está ativa, em oposição ao estado descartável.
1293. [[localstack-testcontainers]] — A biblioteca de contêineres de teste permite iniciar o serviço emulado durante a execução dos testes, com ciclo de vida controlado pela suíte.
1294. [[localstack-terraform-hooks]] — Arquivos de infraestrutura podem servir de gancho de inicialização por meio de extensão, criando recursos automaticamente na subida.
1295. [[localstack-aws-cli-and-tools]] — Um invólucro da ferramenta de linha de comando da nuvem aponta automaticamente para o ambiente emulado, simplificando a preparação.
1296. [[localstack-ci-integration]] — O serviço pode ser iniciado como contêiner no trabalho de integração, com os ganchos preparando os recursos antes da suíte.
1297. [[localstack-limits-and-practices]] — A emulação cobre um subconjunto de serviços e comportamentos, e diferenças sutis de permissão, limites e integração podem não aparecer.

### Terratest — testes de infraestrutura, destruição, repetição e estágios

1298. [[terratest-basic-test]] — O teste é escrito na linguagem de programação do projeto e usa os módulos da biblioteca para inicializar, aplicar e consultar os recursos declarados.
1299. [[terratest-destroy]] — A destruição dos recursos é agendada no início do teste para executar ao final, inclusive quando verificações falham no meio.
1300. [[terratest-stages]] — A biblioteca de estágios permite separar aplicação, verificação e destruição em blocos que podem ser executados isoladamente por variáveis de ambiente.
1301. [[terratest-retries]] — Funções de repetição reexecutam operações que dependem de propagação assíncrona, com número de tentativas e intervalo configuráveis.
1302. [[terratest-unique-resources]] — A biblioteca oferece geração de identificadores aleatórios usados para nomear recursos de forma que execuções concorrentes não colidam.
1303. [[terratest-verify-state]] — Depois da aplicação, os auxiliares consultam o provedor para confirmar que o recurso existe e apresenta as propriedades esperadas, em vez de confiar apenas na saída declarada.
1304. [[terratest-http-checks]] — Auxiliares de rede repetem requisições até obter o código esperado e o conteúdo previsto, validando o serviço do ponto de vista do usuário.
1305. [[terratest-parallelism-and-cost]] — Os casos podem ser marcados para execução paralela, e a escolha de regiões e tipos de recurso afeta diretamente o custo da suíte.
1306. [[terratest-ci-integration]] — A execução na esteira exige credenciais com permissões mínimas, região definida e limites de tempo e de recursos.
1307. [[terratest-limits-and-practices]] — Testes de infraestrutura são lentos, custam recursos reais e dependem do provedor, complementando a análise estática e os testes de unidade da configuração.

### Checkov — políticas como código, supressões, linha de base e esteira

1308. [[checkov-frameworks]] — A ferramenta identifica o tipo de configuração pelo conteúdo e oferece verificações específicas para cada estrutura suportada.
1309. [[checkov-running-checks]] — A execução aceita lista de verificações a rodar, lista de exclusão e filtro por padrão de identificador.
1310. [[checkov-suppressions]] — Uma anotação no próprio arquivo registra a aceitação do risco, com identificador da verificação e motivo declarado.
1311. [[checkov-baseline]] — A criação de linha de base registra os achados existentes em arquivo, e as execuções seguintes comparam contra esse registro.
1312. [[checkov-secrets]] — O verificador de segredos procura credenciais e chaves por padrões, palavras-chave e análise de entropia em arquivos e blocos de configuração.
1313. [[checkov-custom-policies]] — Políticas próprias podem ser escritas em linguagem de programação ou em formato declarativo e mantidas junto ao projeto.
1314. [[checkov-output-and-ci]] — A execução gera saída legível e formatos estruturados, e a esteira pode falhar por política ou apenas reportar.
1315. [[checkov-terraform-checks]] — As verificações de configuração declarada avaliam atributos de recursos, como exposição pública, criptografia, registros e políticas de acesso.
1316. [[checkov-kubernetes-checks]] — As verificações de manifestos cobrem segurança de contêineres, limites de recurso, privilégios, redes e controles de escalonamento.
1317. [[checkov-limits-and-practices]] — A análise verifica configuração declarada e não substitui teste de comportamento, verificação de permissões efetivas nem avaliação de risco de negócio.

### BackstopJS — regressão visual, cenários, seletores e aprovação de imagens

1318. [[backstopjs-workflow]] — O fluxo gera capturas de referência, produz novas capturas na execução de teste e compara pixel a pixel contra a referência aprovada.
1319. [[backstopjs-scenarios]] — Cada cenário declara rótulo, endereço e opções que definem o estado da página no momento da captura.
1320. [[backstopjs-selectors]] — O cenário pode capturar o documento inteiro, a área visível ou um conjunto de seletores, isolando regiões específicas da página.
1321. [[backstopjs-readiness]] — O cenário pode esperar por seletor presente, evento registrado no console, tempo fixo ou interação prévia antes de capturar.
1322. [[backstopjs-mismatch-threshold]] — O limite define a porcentagem de pixels diferentes aceita antes de o cenário ser marcado como falho, e a exigência de mesmas dimensões pode ser ativada.
1323. [[backstopjs-hiding-dynamic-content]] — O cenário pode ocultar ou remover seletores antes da captura, eliminando do quadro relógios, avisos e dados que mudam a cada acesso.
1324. [[backstopjs-viewports]] — A configuração declara tamanhos de tela com rótulo e dimensões, aplicados a todos os cenários ou sobrescritos por cenário.
1325. [[backstopjs-reports-and-approval]] — O relatório apresenta comparação lado a lado com destaque da diferença, e o comando de aprovação promove as capturas recentes a novas referências.
1326. [[backstopjs-ci-integration]] — A ferramenta roda em ambiente automatizado, com contêiner ou instalação de dependências, e publica relatório estático como artefato.
1327. [[backstopjs-limits-and-practices]] — A verificação mede diferença de pixels, não julga se a mudança é aceitável, e depende de ambiente estável para ser confiável.

### ReportPortal — lançamentos, itens, atributos, histórico e análise

1328. [[reportportal-launches-and-items]] — Cada execução é registrada como lançamento, e os resultados são itens hierárquicos de suíte, teste, cenário e passo sob esse lançamento.
1329. [[reportportal-attributes]] — Atributos são pares de chave e valor anexados ao lançamento ou ao item e usados em filtros, colunas e agrupamentos.
1330. [[reportportal-system-attributes]] — Atributos de sistema alteram o comportamento da plataforma, disparando análise imediata, tratando itens ignorados ou marcando reversões.
1331. [[reportportal-defect-classification]] — A plataforma agrupa falhas por semelhança de mensagem e rastro, permitindo atribuir tipo de defeito e investigar por grupo.
1332. [[reportportal-history-and-uniqueness]] — A plataforma liga execuções históricas do mesmo caso por identificador derivado da localização no código e dos parâmetros, que pode ser definido explicitamente.
1333. [[reportportal-attachments-and-logs]] — Logs e anexos podem ser enviados para o item ou passo correspondente, ficando disponíveis junto do resultado da execução.
1334. [[reportportal-framework-integration]] — Cada framework possui agente que envia os resultados automaticamente, configurado por arquivo de projeto e identificação do lançamento.
1335. [[reportportal-modes-and-projects]] — Um lançamento pode rodar em modo de depuração, visível apenas para o autor, ou no modo padrão do projeto, e a plataforma separa dados por projeto.
1336. [[reportportal-dashboards-and-filters]] — A plataforma permite filtrar execuções e itens por período, nome, atributos e estado, além de montar colunas personalizadas e visões salvas.
1337. [[reportportal-limits-and-practices]] — A plataforma agrega e organiza resultados, mas não executa testes nem garante que o conteúdo reportado reflita o comportamento real.

### ArchUnit — regras de arquitetura, camadas, ciclos e congelamento de violações

1338. [[archunit-import-and-rules]] — A biblioteca importa as classes compiladas para uma estrutura consultável e expressa regras verificáveis com integração ao framework de testes.
1339. [[archunit-layered-architecture]] — Regras de camadas definem grupos por padrão de pacote e restringem quais camadas podem acessar quais outras.
1340. [[archunit-slices-and-cycles]] — Regras de fatias dividem os pacotes segundo um padrão com grupos de captura e verificam se as fatias resultantes estão livres de ciclos.
1341. [[archunit-dependency-rules]] — Regras expressam proibições e permissões de dependência por pacote, nome de classe, anotação ou camada da aplicação.
1342. [[archunit-coding-rules]] — Regras de codificação verificam nomes, anotações, modificadores, exceções declaradas e uso de recursos proibidos.
1343. [[archunit-freezing]] — O congelamento registra as violações atuais em armazenamento próprio e passa a reportar apenas violações novas a cada execução.
1344. [[archunit-onion-and-diagrams]] — A biblioteca oferece regra pronta para o estilo em camadas concêntricas e verificação de aderência a diagrama de componentes.
1345. [[archunit-test-organization]] — As regras podem ser agrupadas por tema em classes próprias e executadas junto da suíte normal do projeto.
1346. [[archunit-ci-failures]] — A falha da verificação interrompe a construção e traz a lista das violações com as classes envolvidas.
1347. [[archunit-limits-and-practices]] — A análise cobre estrutura de classes e dependências no bytecode, sem avaliar qualidade de desenho, desempenho nem coerência semântica das fronteiras.

### Insta — snapshots, revisão, snapshots embutidos e redação em Rust

1348. [[insta-snapshot-basics]] — A macro captura a representação do valor e compara com o arquivo de referência, gravando o novo resultado quando não existe referência.
1349. [[insta-review-workflow]] — A ferramenta de linha de comando apresenta as diferenças em modo interativo, permitindo aceitar, rejeitar ou adiar cada proposta.
1350. [[insta-snapshot-files]] — As referências ficam em diretório ao lado do arquivo de teste, com nome derivado do módulo e do nome informado ou inferido do caso.
1351. [[insta-inline-snapshots]] — Instantâneos embutidos guardam a referência como texto no arquivo de teste, marcado por sinal próprio, e a ferramenta atualiza o trecho ao aceitar.
1352. [[insta-update-modes]] — O modo de atualização define se novas referências são gravadas, se a execução apenas compara ou se valores são sobrescritos sem proposta prévia.
1353. [[insta-redactions]] — Redações substituem valores dinâmicos por marcador fixo ou por valor calculado por função, mantendo a referência estável entre execuções.
1354. [[insta-format-and-serialization]] — A biblioteca compara valores formatados e oferece representações específicas para estruturas serializáveis em formatos legíveis.
1355. [[insta-snapshot-assertions]] — Quando o caso produz mais de uma referência, a ferramenta pode coletar todas as propostas em uma única execução de revisão.
1356. [[insta-snapshot-context]] — A configuração de contexto permite anexar informações como descrição e parâmetro à referência e controlar o que aparece no cabeçalho.
1357. [[insta-ci-and-limits]] — A suíte roda na esteira em modo estrito, e a ferramenta de revisão é opcional, mantendo a verificação independente de passos manuais.
1358. [[insta-vs-other-assertions]] — Instantâneos servem a saídas formatadas e estáveis, enquanto asserções específicas comunicam melhor a intenção de regras de negócio.

## Tranche 20 — especificações de negócio, automação de navegador, dublês, propriedades e carga

### Gauge — especificações em markdown, passos, conceitos e execução paralela

1359. [[gauge-specifications]] — Uma especificação é um arquivo em formato markdown com cabeçalho próprio, uma ou mais seções de cenário e passos como itens de lista.
1360. [[gauge-steps-implementation]] — Cada passo da especificação corresponde a um método anotado no código do projeto, com parâmetros extraídos do texto do próprio passo.
1361. [[gauge-concepts]] — Conceitos combinam uma sequência de passos em uma unidade nomeada, declarada em arquivo próprio e usada como qualquer outro passo.
1362. [[gauge-tags-and-filtering]] — Especificações e cenários podem receber etiquetas, e a execução aceita expressões com conjunção, disjunção e negação sobre elas.
1363. [[gauge-context-and-hooks]] — A execução oferece ganchos de suíte, especificação, cenário e passo, e um contexto próprio para guardar valores entre passos.
1364. [[gauge-data-driven]] — Uma tabela antes de um cenário transforma o bloco em várias execuções, uma por linha, com os valores disponíveis nos passos.
1365. [[gauge-parallel-execution]] — A execução aceita especificações em paralelo, distribuindo-as entre processos ou threads conforme o número de fluxos configurado.
1366. [[gauge-environments-and-config]] — O projeto mantém diretórios de ambiente com arquivos de propriedades, e uma execução escolhe o ambiente pelo nome.
1367. [[gauge-reports-and-ci]] — Cada execução gera relatórios, incluindo o formato navegável em HTML e relatórios estruturados de acordo com os plugins instalados.
1368. [[gauge-limits-and-practices]] — A ferramenta organiza especificações executáveis em linguagem natural, mas não substitui testes de unidade, verificação de contrato nem medição de desempenho.

### Behave — cenários Gherkin, definições de passo, ganchos e fixtures em Python

1369. [[behave-feature-files]] — Cada funcionalidade é descrita em arquivo com estrutura de Gherkin: contexto opcional, cenários e passos com palavras-chave.
1370. [[behave-step-definitions]] — Funções decoradas associam cada passo do texto a código Python, com parâmetros capturados por expressões no padrão do passo.
1371. [[behave-context-sharing]] — O contexto é um objeto passado a cada passo, onde valores são guardados para uso posterior dentro do mesmo cenário.
1372. [[behave-hooks]] — O arquivo de ambiente define funções executadas antes e depois da suíte, da funcionalidade, do cenário e do passo.
1373. [[behave-tags-and-selection]] — Etiquetas podem ser aplicadas a funcionalidades e cenários, e a execução aceita expressões para incluir ou excluir grupos.
1374. [[behave-fixtures]] — Fixtures encapsulam preparação e limpeza com rendimento, podendo ser associadas a etiquetas específicas nos ganchos.
1375. [[behave-configuration]] — A configuração do projeto declara caminhos, formato de saída, comportamento de captura e opções como diretório de relatórios.
1376. [[behave-reports-and-ci]] — A execução pode gerar relatórios em formatos legíveis e estruturados, e o processo termina com código de saída conforme o resultado.
1377. [[behave-django-flask-integration]] — A documentação cobre a integração com aplicações web em Python, incluindo preparação de banco de dados de teste e servidor local.
1378. [[behave-limits-and-practices]] — A ferramenta executa cenários em linguagem natural apoiados por código, sem substituir testes de unidade nem medir desempenho.

### MockServer — expectativas, correspondência, verificação, proxy e contratos

1379. [[ms-expectations]] — Uma expectativa declara o pedido que deve corresponder e a ação a executar, com limites opcionais de número de usos, validade e prioridade.
1380. [[ms-request-matchers]] — Os correspondentes cobrem método, caminho, consulta, cabeçalhos, cookies e corpo, com comparação exata, por padrão ou por esquema.
1381. [[ms-verification]] — A verificação consulta os pedidos registrados e confirma a quantidade de ocorrências, podendo exigir um número exato, mínimo ou máximo.
1382. [[ms-response-verification]] — Quando a verificação inclui correspondência de resposta, a contagem passa a considerar os pares de pedido e resposta registrados no proxy.
1383. [[ms-proxy-and-record-replay]] — No modo proxy, o pedido é encaminhado ao serviço real e o par pedido e resposta fica registrado, podendo ser recuperado como expectativa reutilizável.
1384. [[ms-openapi-contract]] — Uma especificação de interface pode gerar expectativas automaticamente e servir como correspondente para verificar se os pedidos recebidos respeitam o contrato.
1385. [[ms-tests-and-junit]] — O serviço pode ser iniciado durante a suíte, com terminadores e regras de ciclo de vida que sobem e derrubam o servidor por classe ou por execução.
1386. [[ms-scenarios-and-state]] — Cenários permitem que a resposta mude conforme as interações anteriores, avançando o estado a cada correspondência.
1387. [[ms-diagnostics-and-logs]] — O serviço expõe os pedidos recebidos, as expectativas registradas e as mensagens de erro de correspondência, consultáveis durante a execução.
1388. [[ms-limits-and-practices]] — A ferramenta simula e verifica interações em nível de protocolo, sem validar a lógica interna do serviço nem substituir testes de contrato entre consumidor e provedor.

### Keploy — gravação de tráfego, mocks de dependências e repetição na esteira

1389. [[keploy-record-replay]] — A ferramenta observa o tráfego recebido pela aplicação em execução e grava cada pedido com a resposta devolvida como um caso de teste.
1390. [[keploy-dependency-mocks]] — Durante a gravação, as chamadas de saída da aplicação são capturadas e gravadas como mocks, incluindo banco, cache, filas e serviços externos.
1391. [[keploy-replay-in-ci]] — No modo de repetição, os pedidos gravados são reenviados, os mocks são servidos no lugar das dependências e o resultado é comparado com o registro.
1392. [[keploy-test-assertions]] — O caso gravado compara a resposta devolvida na repetição com a resposta registrada, campo a campo, sinalizando diferenças.
1393. [[keploy-deduplication]] — A ferramenta aplica deduplicação sobre o tráfego gravado, mantendo um conjunto menor de casos representativos.
1394. [[keploy-coverage-report]] — A execução de repetição pode coletar cobertura de linhas e ramos da aplicação, indicando o que o tráfego gravado exercitou.
1395. [[keploy-kubernetes-and-sandbox]] — A gravação pode ocorrer em ambiente conteinerizado, capturando tráfego de serviços em execução e reproduzindo-o depois em outro ambiente.
1396. [[keploy-multi-language]] — A captura ocorre na camada de rede e funciona com aplicações escritas em diferentes linguagens, sem alteração no código da aplicação.
1397. [[keploy-legacy-and-migration]] — A captura na camada de rede permite gerar verificação para aplicações sem testes e comparar o comportamento antes e depois de uma migração.
1398. [[keploy-limits-and-practices]] — A gravação cobre os caminhos exercitados e suas dependências, sem substituir testes de unidade nem fluxos de ponta a ponta com sistemas reais.

### Selenide — waits automáticos, coleções, objetos de página e relatórios

1399. [[selenide-basics]] — A biblioteca expõe abertura de página e consulta por seletor com métodos curtos, retornando elementos ou coleções.
1400. [[selenide-smart-waits]] — Verificações e ações aguardam a condição até o limite configurado, repetindo a consulta em vez de falhar de imediato.
1401. [[selenide-collections]] — Consultas com cifrão duplo retornam coleções com filtros, verificação de tamanho e extração de textos e atributos.
1402. [[selenide-page-objects]] — Objetos de página encapsulam os seletores e as operações de cada tela em métodos públicos, sem necessidade de anotações nem inicialização especial.
1403. [[selenide-conditions]] — As condições cobrem existência, visibilidade, texto exato ou parcial, atributos, valores e estados de habilitação e seleção.
1404. [[selenide-screenshots-and-reports]] — A biblioteca captura telas em falhas e pode integrar-se a relatórios, com configuração por propriedades do projeto.
1405. [[selenide-configuration]] — As propriedades definem navegador, endereço remoto, tamanho de janela, limite de espera, captura de tela e pasta de downloads.
1406. [[selenide-headless-and-parallel]] — A execução pode ocorrer sem interface gráfica e com casos distribuídos em paralelo, desde que cada caso controle o próprio estado.
1407. [[selenide-migration-from-selenium]] — A biblioteca é construída sobre a interface de navegador e permite substituir esperas e verificações manuais por operações com espera embutida.
1408. [[selenide-limits-and-practices]] — A biblioteca simplifica a escrita de testes de interface sobre a interface de navegador, sem substituir testes de unidade, de integração nem de desempenho.

### AssertJ — asserções fluentes, coleções, descrições e asserções suaves

1409. [[assertj-fluent-basics]] — A biblioteca oferece um ponto de entrada que devolve um objeto de asserção específico do tipo, com métodos encadeáveis.
1410. [[assertj-collections]] — Existem asserções próprias para listas, conjuntos, mapas e fluxos, cobrindo conteúdo, ordem, presença de elementos e extração de campos.
1411. [[assertj-descriptions]] — O encadeamento permite anexar uma descrição que aparece na mensagem de falha, identificando o que estava sendo verificado.
1412. [[assertj-soft-assertions]] — O objeto de asserções suaves coleta os erros de várias verificações e os reporta juntos ao final do bloco.
1413. [[assertj-junit-integration]] — A biblioteca oferece integração com o framework de testes, injetando o objeto de asserções suaves e reportando os erros automaticamente ao final do caso.
1414. [[assertj-custom-assertions]] — O projeto permite estender as classes de asserção para criar verificações específicas do domínio, publicáveis como ponto de entrada próprio.
1415. [[assertj-exceptions]] — As asserções de exceção verificam tipo, mensagem, causa e presença de trechos na mensagem, sem captura manual de try e catch.
1416. [[assertj-recursive-and-fields]] — A biblioteca permite comparar objetos campo a campo, ignorando ou incluindo campos escolhidos, e comparar estruturas aninhadas recursivamente.
1417. [[assertj-database-and-modules]] — Projetos complementares oferecem asserções para tipos de bancos de dados relacionais, coleções de bibliotecas conhecidas e outras estruturas específicas.
1418. [[assertj-limits-and-practices]] — A biblioteca melhora a expressão e a mensagem das verificações, mas não substitui a escolha do que verificar nem cobre desempenho ou interface.

### MockK — dublês em Kotlin, relaxamento, verificação, slots e corrotinas

1419. [[mockk-basics]] — A biblioteca cria dublês de tipos Kotlin e define o comportamento esperado em blocos que descrevem a chamada e o valor devolvido.
1420. [[mockk-strict-vs-relaxed]] — No modo estrito, chamadas sem resposta definida falham; no modo relaxado, o dublê devolve valores vazios ou neutros automaticamente.
1421. [[mockk-verification]] — Blocos de verificação confirmam que a chamada ocorreu, com quantidade exata, faixa de ocorrências e ordem entre chamadas.
1422. [[mockk-slots-and-capture]] — Um slot registra o valor recebido por uma chamada, permitindo verificar detalhes do argumento depois da execução.
1423. [[mockk-coroutines]] — As funções de suspensão são configuradas e verificadas por variantes com prefixo próprio, que executam os blocos em contexto de corrotina.
1424. [[mockk-objects-and-statics]] — A biblioteca cobre objetos únicos, métodos estáticos, funções de nível superior, extensões e construtores, com limpeza explícita ao final.
1425. [[mockk-configuration]] — Um arquivo de configuração permite definir relaxamento global, registro de chamadas privadas, relaxamento de funções sem retorno e classes que não podem ser dubladas.
1426. [[mockk-relaxed-unit-and-defaults]] — Além do relaxamento comum, a biblioteca oferece relaxamento de funções sem retorno e possibilidade de configurar respostas padrão por tipo.
1427. [[mockk-chained-and-hierarchies]] — Dublês podem devolver outros dublês, permitindo representar cadeias de dependências em estruturas complexas.
1428. [[mockk-limits-and-practices]] — Dublês verificam interações no nível da linguagem, sem substituir testes de integração nem comprovar o comportamento do sistema real.

### fast-check — teste por propriedades, geradores, redução de casos e modelos

1429. [[fc-properties-basics]] — Uma propriedade combina geradores de entrada com um predicado que deve valer para todos os valores produzidos.
1430. [[fc-arbitraries]] — Os geradores descrevem domínios de valores por tipo, com versões para inteiros, textos, listas, registros, opções e combinações.
1431. [[fc-custom-arbitraries]] — Geradores existentes podem ser transformados por mapeamento ou encadeados quando a próxima entrada depende do valor anterior.
1432. [[fc-shrinking]] — Ao encontrar falha, a ferramenta reduz a entrada ao menor caso que ainda reproduz o erro, exibindo o valor mínimo.
1433. [[fc-seed-and-reproducibility]] — Cada execução usa uma semente, exibida na falha, que permite repetir exatamente a sequência de valores gerados.
1434. [[fc-model-based]] — A biblioteca permite descrever comandos, modelo de referência e verificações de invariantes para testar sequências de operações.
1435. [[fc-async-properties]] — Existe variante de propriedade para predicados assíncronos, integrando-se a ambientes de teste com espera pela resolução.
1436. [[fc-number-of-runs-and-ci]] — A execução permite configurar a quantidade de rodadas, o tempo máximo por caso e a política de falha, e integra-se a executores de teste conhecidos.
1437. [[fc-integration-with-runners]] — A biblioteca se integra a executores conhecidos, incluindo extensões que produzem casos de teste a partir de propriedades.
1438. [[fc-limits-and-practices]] — Propriedades verificam invariantes gerais sobre dados gerados, sem provar ausência de erro nem cobrir desempenho ou integração real.

### Robolectric — testes de unidade Android na JVM, sombras e configuração de SDK

1439. [[robolectric-jvm-tests]] — A ferramenta executa código Android na máquina virtual da linguagem, substituindo chamadas ao sistema por implementações próprias.
1440. [[robolectric-sdk-configuration]] — A execução pode declarar a versão do sistema Android em nível de classe, de pacote ou de arquivo de propriedades.
1441. [[robolectric-shadows]] — Sombras são implementações próprias que substituem classes do sistema, com métodos que devolvem valores controlados e registram o efeito das chamadas.
1442. [[robolectric-activity-lifecycle]] — A biblioteca oferece construção controlada de telas, permitindo criar, iniciar, retomar, pausar e destruir conforme o cenário exige.
1443. [[robolectric-resources-and-qualifiers]] — A execução carrega recursos do projeto e permite escolher qualificadores, como idioma, orientação e densidade de tela.
1444. [[robolectric-java-version-compatibility]] — Versões recentes da máquina virtual exigem abertura explícita de módulos internos para que a biblioteca acesse classes do sistema.
1445. [[robolectric-dependencies-and-offline]] — A biblioteca baixa artefatos das versões do sistema em tempo de execução, e o endereço de repositório pode ser configurado.
1446. [[robolectric-frameworks-integration]] — A execução convive com bibliotecas de asserção, dublês e execução paralela, mantendo o mesmo padrão dos testes comuns.
1447. [[robolectric-vs-instrumented]] — Testes na JVM rodam rápido e cobrem lógica e ciclo de vida simulado; testes instrumentados exercitam o sistema real em aparelho ou emulador.
1448. [[robolectric-limits-and-practices]] — A simulação cobre grande parte das interfaces do sistema, mas não reproduz desempenho, hardware, nem o comportamento exato de versões de aparelhos.

### NBomber — carga em .NET, simulações, cenários, limites e relatórios

1449. [[nb-scenarios-basics]] — O cenário descreve a operação a executar em cada iteração, em código da própria linguagem, e devolve o resultado da operação.
1450. [[nb-load-simulations]] — As simulações descrevem o ritmo de injeção de iterações, incluindo taxa constante, taxa crescente com rampa e número fixo de cópias.
1451. [[nb-steps-and-metrics]] — Passos separam etapas da operação, cada uma com medidas próprias de latência, contagem e tamanho, agregadas ao resultado do cenário.
1452. [[nb-warmup-and-duration]] — A execução pode incluir fase de aquecimento antes da medição e define a duração de cada simulação separadamente.
1453. [[nb-assertions-and-thresholds]] — A execução permite declarar limites sobre as métricas, como percentual de falhas e percentil de latência, avaliados ao final do teste.
1454. [[nb-reports-and-sinks]] — Cada execução gera relatório navegável, e a integração com sistemas de acompanhamento permite publicar métricas em tempo real.
1455. [[nb-http-metrics-and-plugins]] — Extensões adicionam métricas específicas de protocolo, como tempos de conexão, reutilização de conexões e volume trafegado.
1456. [[nb-data-feeds-and-realism]] — A biblioteca permite fornecer dados variados por iteração, aproximando a carga do padrão real de uso.
1457. [[nb-distributed-cluster]] — A execução pode ser distribuída entre agentes coordenados, somando a carga de várias máquinas e agregando os resultados.
1458. [[nb-ci-integration]] — A ferramenta integra-se a executores de teste conhecidos, permitindo que a carga faça parte do trabalho automatizado.
1459. [[nb-limits-and-practices]] — A ferramenta mede carga gerada em código e produz métricas confiáveis, mas não identifica a causa raiz nem substitui a análise de desempenho do sistema.

## Tranche 21 — executores de navegador e de unidade, asserções, dublês, cassetes HTTP, mutação e fuzzing

### Nightwatch — framework integrado de testes de navegador com WebDriver

1460. [[nightwatch-integrated-framework]] — O Nightwatch é um framework completo, escrito em Node.js, para testes de ponta a ponta de sites em vários navegadores, usando a API W3C WebDriver.
1461. [[nightwatch-browser-drivers]] — O controle dos navegadores acontece por serviços que implementam o protocolo WebDriver: GeckoDriver, ChromeDriver, Microsoft Edge Driver e SafariDriver.
1462. [[nightwatch-settings-basics]] — A configuração central do Nightwatch define src_folders para localizar os testes, test_settings para declarar ambientes e os objetos webdriver ou selenium para o transporte.
1463. [[nightwatch-environments-baseurl]] — A propriedade baseUrl (também grafada base_url, launch_url ou launchUrl) fica disponível na API do teste e assume o valor do ambiente selecionado na execução.
1464. [[nightwatch-capabilities-desired]] — O objeto desiredCapabilities (ou capabilities) define as capacidades da sessão WebDriver, como o nome do navegador e opções de toleração de certificados.
1465. [[nightwatch-page-objects-path]] — A chave page_objects_path aponta as pastas de onde os objetos de página são carregados e ficam disponíveis pelo namespace page da API do teste.
1466. [[nightwatch-custom-commands-assertions]] — As chaves custom_commands_path e custom_assertions_path registram pastas de comandos e asserções definidos pelo projeto, anexados à API do teste.
1467. [[nightwatch-parallel-test-workers]] — A chave test_workers aceita verdadeiro ou um objeto com enabled e workers, rodando cada suíte em um processo próprio com número de trabalhadores fixo ou automático.
1468. [[nightwatch-runner-mocha-unit]] — O campo test_runner seleciona o runner interno (default) ou o mocha, com opções aninhadas como ui; unit_tests_mode desliga a criação automática da sessão de navegador.
1469. [[nightwatch-screenshots-failures]] — O objeto screenshots controla a geração de imagens quando um comando erra ou um teste falha, com chaves enabled, on_failure, on_error e path.

### AVA — executor de testes de Node.js com concorrência e isolamento por arquivo

1470. [[ava-concurrency-model]] — No AVA, os testes de um arquivo são definidos para rodar concorrentemente, e o executor só espera um teste terminar quando ele retorna uma promessa ou um observável.
1471. [[ava-worker-isolation]] — Cada arquivo de teste roda em uma thread de worker nova, com opção de voltar a processos separados pela configuração workerThreads, e o NODE_ENV do teste é definido automaticamente.
1472. [[ava-setup-npm-init]] — O comando npm init ava instala o AVA como dependência de desenvolvimento e grava o script test apontando para o binário, já marcando o pacote como módulo ES.
1473. [[ava-declaring-tests]] — Um teste é declarado chamando a função test importada do AVA com um título e a implementação, e o título deve ser único dentro de cada arquivo.
1474. [[ava-async-support]] — O AVA aguarda promessas retornadas pelo teste e falha o caso se a promessa rejeitar, com suporte nativo a funções async e consumo automático de observáveis até o fim.
1475. [[ava-serial-modifier]] — O modificador .serial força testes que não podem dividir o processo a rodarem em sequência, sempre antes dos testes concorrentes do mesmo arquivo.
1476. [[ava-only-skip-todo-failing]] — O modificador .only recorta os casos do arquivo, .skip pula mantendo o caso visível, .todo reserva um placeholder só com título e .failing documenta um defeito esperado sem quebrar a esteira.
1477. [[ava-hooks-lifecycle]] — O AVA registra test.before, test.after, test.beforeEach, test.afterEach e as variantes .always, que executam preparação e limpeza em torno dos testes do arquivo.
1478. [[ava-magic-assert-diffs]] — O AVA amplia as falhas de asserção com trechos de código e diffs limpos entre real e esperado, destacando apenas a diferença em objetos e arrays.
1479. [[ava-parallel-ci-watch]] — O AVA detecta ambientes de CI com builds paralelas (via ci-parallel-vars) e executa em cada build um subconjunto diferente dos arquivos, cobrindo o total somado; o flag --watch reexecuta ao salvar.

### Chai — asserções encadeáveis em linguagem BDD para JavaScript

1480. [[chai-three-styles]] — O Chai oferece expect e should, que compartilham a mesma linguagem encadeável, mais o estilo assert clássico com argumentos posicionais.
1481. [[chai-language-chains]] — Os getters to, be, been, is, that, which, and, has, have, with, at, of, same, but, does, still e also existem para melhorar a legibilidade e não alteram o resultado.
1482. [[chai-not-assert-positive]] — O elo .not nega toda asserção seguinte na cadeia, mas a documentação recomenda afirmar a saída esperada em vez de negar uma entre muitas inesperadas.
1483. [[chai-deep-vs-strict]] — Adicionar .deep à cadeia faz as asserções equal, include, members, keys e property compararem por igualdade profunda em vez da estrita do operador de três sinais de igual.
1484. [[chai-nested-property-paths]] — Com .nested antes de property ou include, o Chai entende notação de ponto e colchetes no nome da chave, como 'a.b[1]', e permite escapar ponto e colchete literais com barras invertidas duplas.
1485. [[chai-own-versus-inherited]] — O elo .own restringe property e include às propriedades próprias do objeto, ignorando o que veio do protótipo.
1486. [[chai-ordered-members]] — O elo .ordered faz asserções members exigirem a mesma sequência dos elementos, e combinado com include a verificação começa alinhada ao início dos dois arrays.
1487. [[chai-any-all-keys]] — Para asserções keys, .any exige ao menos uma das chaves listadas e .all exige todas; o comportamento padrão é .all quando a cadeia não escolhe.
1488. [[chai-type-a-an]] — A asserção .a (ou .an) compara o tipo detectado com a string informada, é insensível a maiúsculas e respeita o Symbol.toStringTag de objetos customizados.
1489. [[chai-include-polymorphism]] — Em string, .include verifica substring; em array, membro presente; em objeto, subconjunto de propriedades; em Set ou WeakSet, membro por SameValueZero; em Map, um dos valores.

### Sinon.JS — espiões, stubs, mocks e relógio falso para testes em JavaScript

1490. [[sinon-purpose-scope]] — O Sinon é uma biblioteca de stubbing, spying e mocking para testes em JavaScript que funciona com qualquer framework de teste unitário.
1491. [[sinon-spy-observation]] — sinon.spy(objeto, "metodo") envolve o método mantendo o comportamento original e registra tudo o que aconteceu com ele durante o teste.
1492. [[sinon-stub-replace-behavior]] — Um stub troca o comportamento de uma função por um resultado escolhido: valores fixos, exceções lançadas ou callbacks disparados sob demanda.
1493. [[sinon-stub-on-existing-method]] — O Sinon permite stubar um método específico de um objeto existente, mantendo os demais métodos da instância funcionando como sempre.
1494. [[sinon-withargs-per-call]] — Com .withArgs, um mesmo stub responde diferente conforme os argumentos recebidos, e variantes como .onCall variam a resposta por ordem de chamada.
1495. [[sinon-mock-expectations]] — O mock do Sinon declara expectativas de chamada sobre o objeto e cobra o cumprimento no fim do teste, em vez de só observar passivamente.
1496. [[sinon-clock-fake-timers]] — sinon.useFakeTimers congela o relógio do ambiente de teste e avança no ritmo escolhido, disparando timeouts e intervalos sob comando.
1497. [[sinon-fake-server-xhr]] — O fake server do Sinon intercepta requisições XMLHttp no navegador de teste, respondendo a roteamentos definidos pelo próprio teste.
1498. [[sinon-sandbox-restore]] — O sandbox agrupa espiões, stubs e relógios criados a partir dele e devolve todos os objetos ao estado original num único restore.
1499. [[sinon-assert-framework-agnostic]] — Além das propriedades booleanas dos dublês, o Sinon expõe um conjunto sinon.assert com falhas descritivas que funcionam com qualquer executor.

### VCR.py — gravação e repetição de interações HTTP em testes Python

1500. [[vcrpy-record-replay-contract]] — O VCR.py grava as interações HTTP reais em um arquivo de cassetete na primeira execução e reproduz as respostas gravadas nas execuções seguintes.
1501. [[vcrpy-context-decorator]] — O cassette pode envolver o código com vcr.use_cassette('caminho.yaml') como gerenciador de contexto ou como decorator sobre a função de teste.
1502. [[vcrpy-record-modes]] — Os modos de gravação controlam quando o VCR fala com a rede: once grava sem cassette e erro com novo pedido, new_episodes estende sempre, none proíbe rede, all regrava tudo.
1503. [[vcrpy-vcrtestcase]] — Herdar de vcr.unittest.VCRTestCase liga a gravação e a reprodução automaticamente a cada teste, com o cassette acessível em self.cassette e caminho padrão cassettes/Classe.metodo.yaml.
1504. [[vcrpy-vcrmixin]] — Quando a classe de teste já herda de outra base de testes, o VCRMixin entra como mixin na frente do TestCase para obter a mesma gravação automática.
1505. [[vcrpy-vcr-config-object]] — Instanciar vcr.VCR com serializer, cassette_library_dir, record_mode e match_on cria uma configuração reutilizável, e cada use_cassette aceita overrides que vencem o global.
1506. [[vcrpy-request-matching]] — Por padrão o VCR considera idênticos os pedidos com mesmo método, esquema, host, porta, caminho e query, e a lista match_on aceita também uri, body, raw_body, headers e um alias url.
1507. [[vcrpy-pytest-plugins]] — Para o pytest existem duas integrações mantidas fora do núcleo: o plugin pytest-vcr e o pytest-recording, que também bloqueia o acesso à rede.
1508. [[vcrpy-override-hooks]] — A VCRTestCase expõe _get_vcr_kwargs, _get_cassette_library_dir e _get_cassette_name para reescrever configuração, pasta e nome, e _get_vcr permite registrar matchers antes do uso.
1509. [[vcrpy-when-cassettes-fit]] — O VCR.py cobre a camada HTTP do teste de integração; ele não valida contratos de esquema nem executa o serviço real, e serve como substituto de ambiente, não de suíte.

### freezegun — congelamento e viagem do relógio em testes Python

1510. [[freezegun-what-it-mocks]] — O freezegun congela o tempo dos testes simulando o módulo datetime: now, utcnow, today, time.time, localtime, gmtime e strftime devolvem o instante escolhido.
1511. [[freezegun-decorator-basics]] — freeze_time aceita uma string de data e funciona como decorator simples sobre a função de teste, valendo por toda a duração do caso.
1512. [[freezegun-class-decorator]] — Aplicado à classe, o decorator congela o tempo em cada callable testável, servindo tanto a TestCase do unittest quanto a classes comuns de teste.
1513. [[freezegun-context-manager]] — O uso com with freeze_time("2012-01-14"): circunscreve o congelamento ao bloco, e fora dele o relógio volta ao normal.
1514. [[freezegun-raw-start-stop]] — O objeto cru devolvido por freeze_time aceita start() e stop() manuais, a peça que permite ligar o congelamento em fixtures e setups compartilhados.
1515. [[freezegun-as-kwarg]] — O parâmetro as_kwarg injeta o objeto do congelador no teste por nome, dando acesso ao time_to_freeze e aos controles de avanço dentro do corpo.
1516. [[freezegun-tz-offset]] — O argumento tz_offset desloca o tempo congelado, aceitando horas inteiras ou um timedelta com minutos fracionários, e separa o que é utcnow do que é now local.
1517. [[freezegun-nice-inputs]] — O parser usa dateutil por baixo, aceitando textos como "Jan 14th, 2012", e freeze_time recebe ainda uma função ou um gerador como fonte de datas.
1518. [[freezegun-tick-modes]] — tick=True mantém o relógio andando a partir do instante congelado, e auto_tick_seconds avança o tempo uma quantidade fixa a cada chamada de now, sobrepondo-se ao tick.
1519. [[freezegun-manual-ticks]] — Usando o contexto como gerenciador, o objeto frozen_datetime permite tick() de um segundo e tick(delta=...) com o salto desejado, e chamá-lo devolve o instante atual congelado.

### mutmut — testes de mutação para Python com resultados acionáveis

1520. [[mutmut-what-mutation-tests]] — A mutação altera sistematicamente o código-fonte e verifica se a suíte falha; um mutante que sobrevive indica comportamento não realmente testado.
1521. [[mutmut-install-first-run]] — pip install mutmut e um mutmut run na raiz do projeto bastam: o mutmut roda o pytest sobre a pasta tests ou test e tenta descobrir sozinho onde fica o código a mutar.
1522. [[mutmut-resume-and-retest]] — O mutmut lembra do trabalho já feito, permitindo parar a corrida a qualquer momento e continuar de onde parou, e o browse retesta mutantes depois de você mexer nos testes.
1523. [[mutmut-browse-tui]] — O mutmut browse abre uma interface de terminal com os mutantes encontrados, onde é possível inspecionar cada um e retestar funções ou módulos inteiros pelas teclas f e m.
1524. [[mutmut-apply-mutant]] — Um mutante pode ser gravado no arquivo-fonte via browse ou pelo comando mutmut apply <mutante>, materializando a mudança exatamente como a corrida a viu.
1525. [[mutmut-fork-requirement]] — O mutmut exige suporte a fork no sistema operacional, o que na prática significa rodar no Windows dentro do WSL.
1526. [[mutmut-config-paths]] — Quando o layout foge do óbvio, a seção [mutmut] do setup.cfg (ou tool.mutmut no pyproject.toml) define source_paths e pytest_add_cli_args_test_selection; no TOML os caminhos viram lista.
1527. [[mutmut-copy-stack-depth]] — Arquivos extras de suporte entram na corrida pela chave also_copy, e max_stack_depth limita a contagem de relevância de um teste à profundidade de pilha dentro do código-fonte.
1528. [[mutmut-mutate-selection]] — Os padrões only_mutate e do_not_mutate filtram arquivos por glob estilo Unix, e mutate_only_covered_lines troca o critério de funções chamadas por linhas cobertas pelo coverage.py.
1529. [[mutmut-typecheck-debug]] — O parâmetro type_check_command permite usar mypy ou pyrefly em JSON para descartar mutantes que nem sequer tipam, e debug=true despeja todo o detalhe que a interface limpa engole.

### cargo-mutants — testes de mutação para Rust sem setup de projeto

1530. [[cargo-mutants-what-it-finds]] — A ferramenta substitui a implementação de funções candidatas por algo trivial e roda os testes: se tudo continua passando, a função não tem teste real.
1531. [[cargo-mutants-install-run]] — cargo install cargo-mutants publica o subcomando, e o trabalho começa com um simples cargo mutants na raiz do crate, sem tocar no código.
1532. [[cargo-mutants-side-effects]] — A documentação adverte que a ferramenta compila e executa código com modificações geradas por máquina: se a suíte escreve ou apaga arquivos, a corrida pode causar estrago real.
1533. [[cargo-mutants-baseline-first]] — Antes de qualquer mutante, a ferramenta roda os testes sem modificação; falhas ali abortam a análise e produzem código de saída quatro dedicado.
1534. [[cargo-mutants-result-vocabulary]] — Cada mutante recebe um de quatro destinos: pego por teste, não pego, verificação de tipos que falhou ou compilação quebrada, cada qual com seu significado de cobertura.
1535. [[cargo-mutants-list-diff-json]] — As opções --list, --diff e --json mostram os mutantes gerados sem executar nada: a primeira a enumeração, a segunda a substituição em diff e a terceira a forma legível por máquina.
1536. [[cargo-mutants-skip-annotation]] — Com a dependência do micro-crate mutants no Cargo.toml, o atributo #[mutants::skip] numa função a remove da lista de mutantes.
1537. [[cargo-mutants-output-directory]] — A corrida cria o diretório mutants.out na raiz, com um arquivo de log por mutante e pelo baseline, contendo o diff aplicado e a saída do cargo, além de mutants.json descrevendo tudo.
1538. [[cargo-mutants-speed-advice]] — Todo ganho de velocidade de cargo build e cargo test se multiplica na corrida, e o README cita o linker Mold no Linux por causa das ligações incrementais intensas.
1539. [[cargo-mutants-hard-to-test]] — Funções que gerenciam caches ou efeitos de performance podem sobreviver à mutação sem poderem ser simplesmente removidas; o README orienta torná-las observáveis ou pular com aviso.

### Toxiproxy — simulação de condições de rede para testes de resiliência

1540. [[toxiproxy-purpose-positioning]] — O Toxiproxy é uma estrutura para simular condições de rede em testes, desenvolvimento e CI, com adulteração determinística das conexões e espaço para caos aleatório.
1541. [[toxiproxy-install-server]] — O servidor é distribuído como binário e pacote (Linux via releases, macOS por Homebrew ou MacPorts, Windows via executável) e roda também como contêiner ghcr.io/shopify/toxiproxy; do fonte é make build.
1542. [[toxiproxy-populate-proxies]] — O mapeamento de endpoints — nome, listen e upstream — é registrado cedo no boot via populate, arquivo config/toxiproxy.json lido com -config ou comandos do toxiproxy-cli create.
1543. [[toxiproxy-latency-bandwidth]] — O toxic latency adiciona atraso igual a latency com variação jitter em milissegundos, e bandwidth limita a conexão a um máximo de KB por segundo.
1544. [[toxiproxy-timeout-reset-peer]] — O toxic timeout bloqueia todo o tráfego e fecha a conexão após timeout milissegundos, ou mantém a queda indefinida com zero; o reset_peer simula TCP RESET imediato ou após o prazo dado.
1545. [[toxiproxy-slicer-limit-data]] — O slicer fatia os dados TCP em pedaços pequenos com delay médio em microssegundos entre fatias, enquanto limit_data fecha a conexão quando o volume transmitido passa do limite em bytes.
1546. [[toxiproxy-packet-loss]] — O toxic packet_loss descarta chunks aleatoriamente com probabilidade loss_rate entre zero e um, e correlation eleva a chance de descarte logo após um descarte anterior, modelando perda em rajada.
1547. [[toxiproxy-toxic-fields-direction]] — Toxicos têm nome padrão tipo_corrente, stream obrigatório upstream (cliente para servidor) ou downstream (servidor para cliente), toxicidade de probabilidade com default um, e atributos próprios; derrubar o serviço é outro gesto, com enabled falso no proxy.
1548. [[toxiproxy-http-api-endpoints]] — Toda manipulação passa pela interface JSON na porta 8474: listar e criar proxies, popular lotes, ler e atualizar proxies e toxics por rota própria, além da listagem de endpoints no README.
1549. [[toxiproxy-clients-ecosystem]] — O projeto mantém cliente Go no repositório e a comunidade atende Ruby, Python, .NET, PHP, Node, Java, Haskell, Rust e Elixir, todos falando com o mesmo daemon.

### Jazzer — fuzzing dirigido por cobertura e em processo para a JVM

1550. [[jazzer-coverage-guided-jvm]] — O Jazzer faz fuzzing dirigido por cobertura, no próprio processo da JVM, gerando e mutando entradas de um método de teste para maximizar o alcance de código e encontrar falhas.
1551. [[jazzer-standalone-binary]] — Os arquivos de release trazem um binário jazzer que sobe a própria JVM já configurada para fuzzing; basta apontar o classpath e a classe do fuzz test.
1552. [[jazzer-main-class-invocation]] — Também é possível invocar com o seu próprio java o classpath do projeto mais jazzer.jar e jazzer-junit.jar e a classe com.code_intelligence.jazzer.Jazzer, passando --target_class com a classe do fuzz test.
1553. [[jazzer-fuzzertestoneinput]] — No modo sem JUnit, o fuzz test é uma classe pública com um método estático fuzzerTestOneInput que declara os parâmetros que o fuzzer vai gerar e variar.
1554. [[jazzer-junit-fuzzing-mode]] — Sob JUnit com @FuzzTest, habilita-se o modo de fuzzing com a variável JAZZER_FUZZ=1 antes de rodar os testes, fazendo o Jazzer executar um fuzz test por vez e gerar entradas livremente.
1555. [[jazzer-generated-corpus]] — Entradas que abrem nova cobertura vão para o diretório gerado em .cifuzz-corpus/<pacote>.<ClasseTeste>/<metodo>, formando o ponto de partida das próximas corridas.
1556. [[jazzer-crash-inputs-directory]] — Toda entrada que provoca falha é salva no diretório de inputs do teste, derivado do pacote e da classe — src/test/resources/<pacote>/<Classe>Inputs/<metodo> — ou no diretório atual quando a pasta não existe.
1557. [[jazzer-gitattributes-binary]] — Para versionar os diretórios de entradas, o README manda marcá-los como binários no .gitattributes, com src/test/resources/** e .cifuzz-corpus/** no exemplo.
1558. [[jazzer-seeding-junit]] — Um @FuzzTest aceita sementes iniciais pelos parameter sources padrão do JUnit — @MethodSource, @CsvSource, @ValueSource ou ArgumentsSource próprios — que rodam como casos na regressão e como base de mutação no fuzzing.
1559. [[jazzer-sanitizers-hooks]] — Os sanitizers (bug detectors) monitoram a execução contra padrões de risco como SSRF, path traversal e injeção de comando, devolvendo feedback que orienta a geração de entradas.

## Tranche 22 — suítes de shell e PowerShell, BDD em .NET, asserções fluent, property testing, mocks e simulação de HTTP e cobertura gcov

### bats-core — testes TAP para scripts de shell

1560. [[bats-what-it-is]] — O Bats (Bash Automated Testing System) é um framework de testes aderente ao TAP para Bash 3.2 ou superior, feito para verificar que os programas UNIX que você escreve se comportam como esperado.
1561. [[bats-test-syntax]] — O arquivo .bats é avaliado como script Bash e cada caso é declarado com @test "descrição" { corpo }, que o pré-processador converte em uma função cujo nome é a descrição do teste.
1562. [[bats-errexit-assertions]] — Os testes Bats rodam sob errexit: o teste termina na primeira linha com status de saída diferente de zero, de modo que toda linha que sobrevive foi verificada.
1563. [[bats-run-status-output]] — O helper run invoca seus argumentos como comando, guarda o código em $status, junta stdout e stderr em $output e sempre retorna 0 para que as asserções seguintes sejam executadas.
1564. [[bats-setup-teardown]] — A dupla setup e teardown funciona como pre- e pós-gancho de cada caso, e a documentação dedica uma seção do tutorial a evitar setups caros repetidos a cada teste.
1565. [[bats-tagging]] — Desde a versão 1.8.0 o Bats traz tags nativas: diretivas # bats test_tags= e # bats file_tags= anexam rótulos aos casos, e --filter-tags decide o que roda combinando os rótulos.
1566. [[bats-focus-mode]] — A tag especial bats:focus faz o Bats filtrar a suíte inteira para executar apenas os casos com ela, e em modo foco o código de saída de uma passada limpa vira 1 de propósito.
1567. [[bats-parallel]] — Por padrão o Bats executa tudo serialmente, mas aceita paralelismo com -j/--jobs quando há GNU parallel (ou substituto compatível) instalado, acelerando suítes cujo gargalo é o custo de processo por teste.
1568. [[bats-formatters]] — O Bats escolhe o formato de saída sozinho: no terminal mostra ✓ e ✗ com resumo humano; sem terminal (CI, pipe) despeja TAP. O flag -F/--formatter força pretty, tap, tap13, junit ou um executável absoluto customizado.
1569. [[bats-fork-history]] — O Bats original de sstephenson parou de evoluir; em 19 de setembro de 2017 a comunidade forkou o projeto no commit 0360811 usando git clone --bare e --mirror para preservar o histórico, e o repositório antigo foi arquivado somente-leitura em 29 de abril de 2021.

### Pester — testes e mocks em PowerShell

1570. [[pester-what-it-is]] — O Pester é simultaneamente framework de testes e de mocking para PowerShell: cobre testes unitários e de integração (sem limitar-se a eles) e serve de base para ferramentas de validação de ambiente e de implantação.
1571. [[pester-naming-discovery]] — O Pester não usa registro explícito de testes: ele descobre casos por convenção de nome — arquivos de teste terminam em .Tests.ps1 — e a execução inteira parte de Invoke-Pester apontando para um caminho.
1572. [[pester-install-module]] — O caminho oficial de instalação é Install-Module Pester -Force seguido de Import-Module Pester -PassThru, que devolve o módulo carregado com sua versão — o exemplo do quick start mostra um Script module versão 6.1.0.
1573. [[pester-dsl-blocks]] — A estrutura de suíte do Pester é Describe contendo Context contendo It; cada It é um caso com título legível, e o BeforeAll no topo do Describe prepara estado e faz o dot-sourcing do código sob teste.
1574. [[pester-assertions-should]] — O lado de afirmação do mini-DSL é o Should: os exemplos oficiais escrevem $result | Should-Be 5 e $allPlanets.Count | Should-Be 8, encadeando o valor real pelo pipeline até a expectativa.
1575. [[pester-mock-basics]] — Mock substitui o comportamento de um comando existente por uma implementação alternativa, e a documentação garante que isso vale para qualquer comando do PowerShell — cmdlet, função ou script — servindo para "shimar" uma camada de dados ou isolar funções complexas.
1576. [[pester-mock-verification]] — A verificação de comportamento fica no Should-Invoke: ele checa se um comando mockado foi chamado, quantas vezes e com quais parâmetros, e a variante -Verifiable cobra ao final todos os mocks marcados como verificáveis.
1577. [[pester-mock-scoping]] — Desde a reescrita do v5, mocks não são mais válidos no Describe inteiro: eles valem apenas no bloco onde foram colocados, o que torna o It que os declara autossuficiente e o teste vizinho imune.
1578. [[pester-mock-advanced]] — Casos difíceis têm resposta própria: comandos nativos são mockados via $args porque não expõem parâmetros nomeados, o mock vê $PesterBoundParameters no lugar de $PSBoundParameters (sobreposto pelo proxy), e no Windows PowerShell 5.1 o cache de classes quebra o Mock.
1579. [[pester-coverage]] — A cobertura do Pester v6 se configura por objeto: New-PesterConfiguration, ligar CodeCoverage.Enabled, opcionalmente restringir com CodeCoverage.Path e chamar Invoke-Pester -Configuration $config — o parâmetro -CodeCoverage direto caiu de uso.

### Reqnroll — BDD Gherkin para .NET

1580. [[reqnroll-what-it-is]] — O Reqnroll é uma ferramenta open-source de automação de testes .NET para praticar BDD: um porte para .NET do Cucumber, baseado no framework e no codebase do SpecFlow, que transforma especificações em *feature files* Gherkin em testes automatizados.
1581. [[reqnroll-platforms-runners]] — O Reqnroll roda nos três sistemas operacionais principais (Windows, Linux, macOS) e nas implementações correntes do .NET — do .NET Framework 4.6.2+ até o .NET 10.0 — usando MsTest, NUnit, xUnit ou TUnit como motor de execução.
1582. [[reqnroll-rename-migration]] — A migração do SpecFlow é majoritariamente renomeação: pacotes SpecFlow.* viram Reqnroll.*, o namespace TechTalk.SpecFlow vira Reqnroll, e classes com SpecFlow no nome (por exemplo ISpecFlowOutputHelper) são renomeadas em consequência.
1583. [[reqnroll-datatable-assist]] — Além da renomeação, a API ganhou ajustes de vocabulário Gherkin: existe agora o alias DataTable para a classe Table, os assistentes de mapeamento viraram "DataTable Helpers" no namespace Reqnroll (usáveis sem using extra) e o container de injeção de dependência mudou de BoDi para Reqnroll.BoDi.
1584. [[reqnroll-cucumber-expressions]] — Os pacotes CucumberExpressions.SpecFlow.* externos não são mais necessários: o Reqnroll traz suporte a Cucumber Expressions embutido, o binding pattern no formato {param} escrito direto no atributo do passo.
1585. [[reqnroll-plugins-actions]] — Os plugins de integração mantidos pelo SpecFlow foram portados (exemplo: Reqnroll.Autofac), e os pacotes SpecFlow.Actions.* — que traziam suporte pronto a tecnologias de automação — vivem como Reqnroll.SpecFlowCompatibility.Actions.*, por exemplo Actions.Selenium.
1586. [[reqnroll-livingdoc]] — O SpecFlow+ LivingDoc era parte fechada do SpecFlow e não pôde ser absorvido pelo Reqnroll; o projeto está reconstruindo uma ferramenta parecida e enquanto isso publica um workaround com o CLI generator do Living Doc do SpecFlow.
1587. [[reqnroll-mstest-outline]] — Com MsTest, o Reqnroll gera testes data-driven a partir de Scenario Outlines, e isso pode conflitar com tooling que filtra por nome — VSTest pipeline task e VSTest.Console.exe entre eles; a guia documenta a incompatibilidade e o caminho para voltar ao comportamento compatível com SpecFlow.
1588. [[reqnroll-license-sponsors]] — A linha de licença separa as peças: o Reqnroll para Visual Studio é licenciado sob BSD 3-Clause (copyright 2024-2026 Reqnroll), o projeto declara basear-se no framework SpecFlow e lista patrocinadores — Spec Solutions, Info Support e TestMu AI — com página própria de sponsorship.
1589. [[reqnroll-setup-guides]] — O README oficial condensa o onboarding em rotas nomeadas: quickstart guide, site reqnroll.net, documentação em docs.reqnroll.net, página de configuração de projeto NuGet, instruções de IDE e release notes — cada uma apontando para o passo correspondente da adoção.

### FluentAssertions — asserções legíveis para .NET

1590. [[fa-what-it-is]] — O FluentAssertions é um conjunto de métodos de extensão .NET que deixa especificar o resultado esperado de um teste TDD ou BDD de forma natural, começando sempre pelo using FluentAssertions que injeta as extensões no escopo.
1591. [[fa-collections-predicate]] — Para coleções, o estilo expressa regra em predicado: numbers.Should().OnlyContain(n => n > 0) afirma que todo elemento satisfaz, e HaveCount aceita um texto "because" que vai direto para a mensagem de erro.
1592. [[fa-exceptions-business-rules]] — As asserções de exceção casam com regras de domínio: action.Should().Throw<RuleViolationException>() encadeia WithMessage com curinga e .And para verificar coleções aninhadas, como Violations.Should().Contain(BusinessRule.CannotChangeIngredientQuantity).
1593. [[fa-which-chaining]] — Sobre coleções e grafos, o Which sobe um nível: dictionary.Should().ContainValue(myClass).Which.SomeProperty.Should().BeGreaterThan(0) afirma dentro do membro encontrado, e o encadeamento continua a corrente.
1594. [[fa-assertion-scope]] — Um AssertionScope batcha várias asserções num bloco using: em vez de parar na primeira quebra, ele acumula e lança uma única exceção no dispose reunindo todos os erros do escopo.
1595. [[fa-framework-detection]] — O FluentAssertions não exige configuração de framework: você adiciona a referência do seu test framework ao projeto e a biblioteca encontra a assembly, usando-a para lançar a exceção específica daquele executor.
1596. [[fa-subject-identification]] — Para imprimir "Expected username to be "jonas" ... but "dennis" has a length of 6", a biblioteca percorre a stack trace, acha arquivo, linha e coluna da chamada e extrai do código-fonte o nome do sujeito — exige debug symbols e build em modo debug, até no build server.
1597. [[fa-beequivalent-to]] — A asserção estrutural entre object graphs é orderDto.Should().BeEquivalentTo(order): todos os membros expostos do grafo expectativa precisam casar por nome e valor com o sujeito, e NotBeEquivalentTo cobre a desigualdade com as mesmas opções.
1598. [[fa-value-semantics]] — Para decidir quando recursar, o FluentAssertions trata como valor qualquer tipo que sobrescreve Object.Equals — mas anonymous types, record, record struct e tuples são sempre comparados por membros, por decisão documentada da comunidade.
1599. [[fa-equivalency-options]] — As opções cobrem os cantos do mapeamento real: WithStrictTyping/WithStrictTypingFor/WithoutStrictTyping regulam o rigor de tipo (por path via IObjectInfo), PreferringRuntimeMemberTypes troca o tipo declarado pelo runtime, e Excluding(o => o.Customer.Name) ou Excluding(ctx => ctx.Path == "Level.Level.Text") cortam membros específicos do grafo.

### jqwik — property-based testing na plataforma JUnit 5

1600. [[jqwik-what-it-is]] — O jqwik é um motor de teste alternativo para a plataforma do JUnit 5: roda standalone ou ao lado de qualquer outro engine, como Jupiter (o padrão) e Vintage (JUnit 4), basta declará-los no mesmo testImplementation.
1601. [[jqwik-gradle-setup]] — A configuração Gradle documentada usa useJUnitPlatform { includeEngines 'jqwik' } — com a variante comentada de incluir mais motores juntos — e filtra classes por **/*Properties.class, **/*Test.class e **/*Tests.class no bloco test.
1602. [[jqwik-property-forall]] — Uma propriedade é um método anotado com @Property — público, protegido ou package-scoped — cujos parâmetros são todos anotados com @ForAll; o jqwik preenche os valores em runtime, por padrão 1000 tries (conjuntos distintos de parâmetros) por propriedade.
1603. [[jqwik-failure-report]] — O bloco de falha do jqwik é um diagnóstico completo: tentativas e checks, modo de geração (RANDOMIZED), política after-failure (SAMPLE_FIRST), quando-fixed-seed (ALLOW), modo e contagem de edge cases (MIXIN, totals e tried) e o seed reproduzível.
1604. [[jqwik-lifecycle]] — A suíte roda com isolamento por desenho: para cada property ou example é criada uma nova instância da classe contêiner, e cada property executa de 1 a n tries cujos argumentos são bindados nos parâmetros @ForAll.
1605. [[jqwik-example-annotation]] — Testes baseados em exemplo não ficam de fora: @Example marca o caso clássico, e internamente o jqwik trata exemplos como propriedades com tries hardcoded em 1 — tudo que funciona para @Property funciona para eles, inclusive geração com @ForAll.
1606. [[jqwik-constraints]] — A geração padrão conhece os tipos (strings, inteiros, listas, mapas, arrays, funcionais) e é ajustada por anotações de restrição nos parâmetros: @IntRange(min = -5, max = 5) delimita inteiros, @AlphaChars restringe o alfabeto, e a seção homônima do guia enumera limites de tamanho de string, char sets, nullabilidade e unicidade.
1607. [[jqwik-provide]] — Quando anotação não basta, o método provedor resolve: um @Provide retorna o Arbitrary para o parâmetro nomeado, e o guia trata ainda suppliers de Arbitrary, providers para tipos embutidos e o catálogo static Arbitraries.* (strings com char ranges, filtros, pesos, embaralhamento).
1608. [[jqwik-shrinking-assumptions]] — O shrinking tenta encontrar amostras menores que ainda falsificam a propriedade; o guia cobre modo integrado, desligar (ShrinkingMode.OFF), modo full e trocar o alvo do shrink, com exemplos onde a string "LVtyB" encolhe para "AA".
1609. [[jqwik-config-modules]] — O guia fecha o ciclo com configuração e alcance: defaults de atributos por classe com @PropertyDefaults, a configuração legada em arquivo jqwik.properties, rerun de propriedades falsificadas, e módulos adicionais — Web (geração de email e domínio), Time (datas, horas e datetimes) e Kotlin (nullable types, coroutines, coleções).

### Kotest property testing — propriedades em Kotlin

1610. [[kotest-proptest-what]] — O property testing do Kotest se executa por duas funções: forAll recebe uma função n-ária (a, ..., n) -> Boolean que deve ser verdadeira para todos os inputs, e checkAll recebe a mesma aridade devolvendo Unit, onde simplesmente se rodam asserções.
1611. [[kotest-checkall-assertions]] — checkAll considera o teste válido enquanto nenhuma exceção for lançada, então o corpo usa as asserções normais do Kotest — a + b shouldHaveLength a.length + b.length é a forma documentada de expresar a propriedade com o vocabulário de asserções do framework.
1612. [[kotest-iterations]] — Por padrão cada propriedade roda 1000 iterações, e o número se muda passando o valor direto na invocação — checkAll<Double, Double>(10_000) roda dez mil amostras daquele teste.
1613. [[kotest-generators]] — Sem especificação, o Kotest resolve um generator por tipo de parâmetro — o de Int cobre negativos, positivos, zeros e infinitos; quando o espaço precisa de recorte, passa-se o gerador explicitamente no lugar dos tipos.
1614. [[kotest-config-maxfailure]] — Toda a afinação do property test passa por PropTestConfig, o objeto de configuração aceito por ambas as funções; maxFailure = 3, por exemplo, tolera até três amostras reprovadas antes de considerar o teste fracassado.
1615. [[kotest-config-listeners-hex]] — O PropTestConfig aceita listeners (PropTestListener registrados via listeners = listOf(...)) que executam setup e teardown dentro de cada iteração da propriedade, não uma vez por teste.
1616. [[kotest-seeds]] — Cada execução sorteia valores a partir de uma semente derivada do kotlin.random.Random default; PropTestConfig(seed = 127305235) fixa a sequência, e PropertyTesting.defaultSeed muda a semente base de todos os testes.
1617. [[kotest-rerun-seeds]] — Por padrão, a semente de uma propriedade que falhou é gravada em ~/.kotest/seeds/<spec>/<testname>; na próxima execução esse seed é detectado e usado no lugar do sorteio aleatório, e o arquivo some quando o teste passa.
1618. [[kotest-proptest-in-specs]] — A doc de property testing vive dentro do framework de specs: todos os exemplos empacotam a propriedade como bloco de teste de um FreeSpec, com hooks, tags e relatório do próprio Kotest — sem executor separado.
1619. [[kotest-proptest-generators-typing]] — A resolução de geradores é feita pelos type parameters da chamada — forAll<String, Int, Boolean> amarra cada posição a um generator — e a mesma lógica permite ao Kotest cobrir aridades de até 14 argumentos sem reflection sobre o lambda.

### Tavern — testes de API declarativos em YAML

1620. [[tavern-what-it-is]] — O Tavern é um plugin do pytest, uma ferramenta de linha de comando e uma biblioteca Python para testes automatizados de APIs com sintaxe YAML simples e flexível, cobrindo REST, APIs MQTT e serviços gRPC.
1621. [[tavern-yaml-structure]] — Todo arquivo de teste tem um ou mais testes, cada teste tem um ou mais stages, e cada stage declara a request feita e a resposta esperada — o vocabulário completo do formato cabe numa página.
1622. [[tavern-file-naming]] — Para o plugin do pytest, a descoberta segue o nome: literalmente só arquivos test_*.tavern.yaml são coletados, e o sufixo duplo .tavern.yaml marca o formato dentro do ecossistema pytest.
1623. [[tavern-pytest-integration]] — A integração recomendada é pip install tavern[pytest] — o extra ativa o plugin — e o próprio guia diz que com pytest instalado basta escrever os YAMLs e rodar: "literalmente tudo que você precisa fazer".
1624. [[tavern-standalone-cli]] — Sem pytest, o CLI tavern-ci --stdout arquivo.tavern.yaml executa a mesma máquina de testes, logando cada teste e cada stage com INFO (tavern.core) e fechando com "PASSED: <stage> [200]".
1625. [[tavern-extensibility]] — A filosofia oficial é quase tudo coberto por declarativo; o que faltar se resolve "caindo" para Python/pytest — fixtures, hooks e o que você já conhece — mantendo o YAML legível no centro.
1626. [[tavern-vs-postman]] — O comparativo oficial assume o terreno: Postman e Insomnia cobrem casos largos de uso de REST, mas o Tavern vence em testes automatizados por validar com Python de verdade, cobrir MQTT/gRPC junto, viver dentro do pytest e manter sintaxe menos verbosa.
1627. [[tavern-python-library]] — Além de plugin e CLI, o Tavern expõe a biblioteca Python para quem integra o motor de testes ao próprio framework ou pipeline de CI — a mesma máquina de stages, chamada por código.
1628. [[tavern-examples-ecosystem]] — A porta de entrada apontada pela doc oficial são as páginas separadas de exemplos (taverntesting.github.io/examples) e a documentação completa (taverntesting.github.io/documentation), com o repositório GitHub logo abaixo.
1629. [[tavern-grpc-mqtt]] — O recorte declarado de protocolos é maior que REST: a página inicial credencia o Tavern para testar APIs RESTful, sistemas baseados em MQTT e serviços gRPC no mesmo formato de stages.

### responses — mocking da biblioteca requests

1630. [[responses-what-it-is]] — O responses é uma biblioteca utilitária para simular (mock out) a biblioteca requests do Python, exigindo Python 3.8+ e requests >= 2.30.0, instalável com pip install responses.
1631. [[responses-register-interface]] — O registro aceita dois formatos: instanciar responses.Response(method="PUT", url=...) e passar o objeto para responses.add, ou chamar add diretamente com os argumentos do Response (método, url, json, status).
1632. [[responses-shortcuts]] — Sete atalhos pré-preenchem o método do registro: responses.delete/get/head/options/patch/post/put aceitam os mesmos argumentos de add com o verbo já resolvido.
1633. [[responses-context-manager]] — Em vez de decorar a função inteira, o with responses.RequestsMock() as rsps registra no objeto do bloco (rsps.add(...)) — e fora do contexto os requests voltam a bater no servidor remoto de verdade.
1634. [[responses-connection-error]] — A regra de falha do responses é seca: uma tentativa de fetch que não atinge nenhum registro levanta ConnectionError do requests — não há fallback para a rede real durante o mock.
1635. [[responses-parameters]] — Os atributos documentados do mock de Response cobrem o essencial do contrato: method, url (string ou expressão regular compilada), body (str, BufferedReader ou Exception), json (configura o Content-Type sozinho), status, content_type (default text/plain), headers e auto_calculate_content_length (desligado por padrão).
1636. [[responses-matchers]] — Em vez de só bater URL, o parâmetro match recebe um iterável de callbacks que casam atributos do request; o módulo responses.matchers traz os prontos: json_params, urlencoded_params, query_param, query_string, kwargs do request, multipart/form-data, headers e fragment identifier.
1637. [[responses-passthru]] — O add_passthru("https://percy.io") abre exceção seletiva ao bloqueio total: pedidos cuja URL casa com o prefixo atravessam o mock e chegam ao servidor real.
1638. [[responses-calls-inspection]] — Depois do bloco, o mock mantém cada interação em responses.calls — o README usa len(responses.calls) como asserção de contagem e .calls[0].request.url para inspecionar o request original.
1639. [[responses-callback]] — Para respostas que dependem do request, responses.add_callback(metodo, url, callback=..., content_type=...) delega a geração da resposta a uma função que recebe o request e devolve a trinca (status, headers, corpo serializado).

### Hoverfly — simulação de APIs por proxy

1640. [[hoverfly-what-it-is]] — O Hoverfly é uma ferramenta leve e open-source de simulação de APIs: substitui dependências lentas e instáveis por simulações realistas e reutilizáveis, com direito a latência de rede, falhas aleatórias e rate limits para exercitar casos extremos.
1641. [[hoverfly-two-binaries]] — A ferramenta são dois binários: hoverfly, o aplicativo que faz o trabalho pesado como proxy server, webserver e endpoints de API, e hoverctl, a CLI que configura e controla o hoverfly — inclusive rodando-o como daemon.
1642. [[hoverfly-capture-mode]] — Em capture mode o hoverfly registra as conversas que passam pelo proxy — requests e respostas do serviço real — e as acumula como simulação reutilizável; o fluxo oficial é hoverctl start, hoverctl mode capture e depois o cliente apontado para o proxy.
1643. [[hoverfly-export-simulation]] — hoverctl export salva as simulações capturadas em arquivos JSON, e o flag --url-pattern aceita string simples ou regex para fatiar o export: um arquivo por recorte de domínio em vez de um amontoado por suíte.
1644. [[hoverfly-stateful-capture]] — Por default o hoverfly guarda um par request/resposta por vez; para APIs stateful — mesma chamada, respostas que mudam — liga-se a gravação com hoverctl mode capture --stateful, que captura a sequência inteira.
1645. [[hoverfly-simulate-mode]] — Em simulate mode o hoverfly responde direto do catálogo de pares gravados, sem tocar no serviço original — o fluxo de trabalho típico termina em hoverctl mode simulate depois de capturar, para testes repetíveis offline.
1646. [[hoverfly-concepts-map]] — A documentação organiza o produto em conceitos nomeados: uso como proxy server e como webserver, modos, simulações, estratégias de matching, caching, templating, estado, destination filtering, middleware, post serve action e a CLI hoverctl — um índice que espelha o vocabulário do produto.
1647. [[hoverfly-troubleshooting]] — A página de troubleshooting oficial tem entradas fixas para as dores típicas: por que um request não casou, por que a melhor resposta aproximada não veio, onde ver logs, o campo deprecatedQuery na simulação, acesso remoto bloqueado e arquivos de simulação inchados por corpos de resposta.
1648. [[hoverfly-java-bindings]] — Além do binário, o ecossistema inclui bindings nativos — o destaque oficial é o Hoverfly Java, com documentação própria em readthedocs — e a promessa de estender e customizar "with any programming language".
1649. [[hoverfly-dev-setup]] — Desenvolver no Hoverfly é Go puro: clonar o repo, make build e os binários caem em target/; make test roda as suítes unitárias e funcionais do projeto — algumas de middleware pedem ruby e python no ambiente.

### gcovr — cobertura de gcov em texto e XML

1650. [[gcovr-what-it-is]] — O gcovr é um utilitário para gerenciar o uso do GNU gcov e gerar sumários de cobertura de código resumidos, com inspiração declarada no coverage.py do Python — um comando de linha alternativo ao lcov que roda o gcov e produz relatórios.
1651. [[gcovr-getting-started]] — O fluxo oficial tem três movimentos: recompilar com --coverage -g -O0, rodar a suíte de testes para gerar os arquivos brutos de cobertura e então invocar gcovr, que imprime o relatório tabular no console.
1652. [[gcovr-root-filter]] — O --root (curto -r) define o diretório das fontes, responde por como os caminhos aparecem reportados (relativos a ele) e, sem nenhum --filter explícito, vira ele próprio o filtro default — o que fica fora da raiz é excluído do relatório.
1653. [[gcovr-output-formats]] — A matriz oficial de saídas cobre --txt (default) e --html/--html-details/--html-nested para humanos, --csv, --json e --json-summary para dados, --markdown e --markdown-summary para PRs, e os dialetos de portal: --clover, --cobertura, --coveralls, --jacoco, --lcov e --sonarqube.
1654. [[gcovr-exclusions]] — A referência traz um arsenal de exclusão declarativa: --exclude-unreachable-branches retira branches de linhas sem código útil (o tal dead code gerado pelo compilador), --exclude-function-lines ignora linhas de definição de função, e --exclude-lines-by-pattern / --exclude-branches-by-pattern operam por regex sobre a linha.
1655. [[gcovr-config-file]] — Cada opção sensata da CLI declara na referência o seu config key homônimo (filter, exclude, gcov-filter, exclude-unreachable-branches...), e o guia mantém uma página "Configuration Files" dedicada a esse modo.
1656. [[gcovr-gcov-parser]] — O guia dedica páginas próprias ao gcov parser e ao "Compiling for Coverage" porque a fidelidade do relatório depende de como o gcovr interpreta os .gcov/.gcda/.gcno e dos flags com que chama o gcov.
1657. [[gcovr-cookbook]] — O cookbook oficial resolve os casos recorrentes que fogem do flow canônico: cobertura de extensões C em Python, builds CMake out-of-source, suporte ao formato Keil uVision e como criar uma aplicação standalone do gcovr.
1658. [[gcovr-versions]] — A documentação versiona explícito: o texto corrente descreve o gcovr 8.6, o changelog abre com 8.6 (13 de janeiro de 2026), 8.5 (8 de janeiro de 2026) e 8.4 (27 de setembro de 2025), e o seletor de versões preserva docs de 4.1 a 7.2.
1659. [[gcovr-vs-lcov]] — A resposta oficial à pergunta "qual a diferença entre gcovr e lcov?" estrutura a escolha: ambos rodam o gcov, mas o gcovr nasceu dos sumários de texto e dos relatórios XML que o lcov não oferecia, mantendo também o HTML com detalhes por arquivo.

## Tranche 23 — runners de navegador para JavaScript, JUnit 4, approval tests, fuzzing em Go/Rust/C/Python, boofuzz, Hyperfoil e Infection

### Karma — execução de testes JavaScript em navegadores reais

1660. [[karma-what-it-is]] — O Karma é descrito no seu README como uma ferramenta simples que permite executar código JavaScript em múltiplos navegadores reais; nasceu no time do AngularJS, que usava o JSTD e queria um runner próprio, estável e rápido, construído sobre Socket.io e Node.js.
1661. [[karma-deprecated-officially]] — O anúncio no topo do README oficial é direto: "Karma is deprecated and is not accepting new features or general bug fixes"; correções críticas de segurança continuam até 12 meses depois de o suporte a Web Test Runner do Angular CLI ser marcado como estável.
1662. [[karma-not-a-framework]] — A doc oficial esclarece um equívoco comum: "Karma is not a testing framework, nor an assertion library"; ele apenas lança o servidor HTTP e gera o test runner HTML, deixando a definição de casos para o framework que você escolher.
1663. [[karma-init-wizard]] — O comando karma init my.conf.js abre um assistente interativo que pergunta, nesta ordem: framework de teste, uso de Require.js, navegadores a capturar automaticamente, localização dos arquivos de código e teste, exclusões, e se o Karma deve observar arquivos e reexecutar ao mudar; no fim grava o arquivo gerado.
1664. [[karma-config-discovery]] — O CLI do Karma aceita o caminho do arquivo como primeiro argumento e, sem ele, procura em ordem: karma.conf.js, karma.conf.coffee, karma.conf.ts, e depois os mesmos nomes dentro de .config/. A função exportada recebe o objeto de configuração e chama config.set.
1665. [[karma-file-patterns]] — As opções que listam caminhos de arquivos — files, exclude e preprocessors — usam a biblioteca minimatch para casar padrões como js/*.js; o basePath resolve todos os caminhos relativos definidos nessas listas e, quando relativo, é interpretado a partir do diretório do próprio arquivo de configuração.
1666. [[karma-browsers-capture]] — A lista browsers inicializa e captura cada navegador listado; ChromeHeadless exige o plugin karma-chrome-launcher, Firefox o karma-firefox-launcher, e assim por diante — e dá para capturar qualquer navegador manualmente abrindo http://localhost:9876/ na mão.
1667. [[karma-timeouts-flakiness]] — A referência documenta browserNoActivityTimeout (padrão 30000 ms) para desconectar quando o navegador para de responder durante os testes; browserDisconnectTimeout (padrão 2000 ms) define quanto esperar o reconector antes de tratar como falha; e browserDisconnectTolerance (padrão 0) quantas desconexões são toleradas antes de o run quebrar.
1668. [[karma-watch-run-once]] — autoWatch (padrão true) habilita observar os arquivos e reexecutar os testes a cada mudança; autoWatchBatchDelay (padrão 250 ms) agrupa múltiplas mudanças em uma única execução usando debounce — o timer reinicia a cada arquivo alterado.
1669. [[karma-frameworks-plugins]] — O aviso no topo da referência de configuração é prático: a maioria dos adaptadores de framework, reporters, preprocessors e launchers precisa ser carregada como plugin; o objeto de configuração não ganha recursos sozinho instalando apenas o pacote karma.

### JUnit 4 — anotações, regras e o modo manutenção do xUnit clássico em Java

1670. [[junit4-maintenance-mode]] — A página oficial define o JUnit como "a simple framework to write repeatable tests", instância da arquitetura xUnit, e logo abaixo crava: "JUnit 4 is in maintenance mode" — apenas bugs críticos e questões de segurança serão corrigidos, e os demais issues e PRs são recusados.
1671. [[junit4-run-without-build]] — O guia oficial de primeiros passos faz o exercício sem build tool: baixe o junit-4.XX.jar da página de releases mais o hamcrest-core-1.3.jar, compile Calculator.java e CalculatorTest.java com javac apontando o classpath para os dois jars e rode java com a classe main org.junit.runner.JUnitCore passando a classe de teste.
1672. [[junit4-fixtures]] — O guia oficial de fixtures define o conceito — um estado fixo de objetos como baseline para testes repetíveis — e enumera as quatro anotações: BeforeClass e AfterClass no nível de classe, Before e After no nível de método; as de classe precisam ser métodos estáticos públicos sem argumentos.
1673. [[junit4-assertthat-hamcrest]] — A página Matcher and assertThat conta a origem: Joe Walnes construiu assertThat sobre o JMock 1, e o time decidiu embuti-lo no JUnit ("We have decided to include this API directly in JUnit"), trazendo pela primeira vez classes de terceiros — as hamcrest-core — para a distribuição.
1674. [[junit4-assertthrows]] — A página oficial de exception testing documenta que o método assertThrows foi adicionado à classe Assert na versão 4.13 e permite afirmar que uma lambda ou referência de método lança um tipo específico de exceção, retornando a exceção para asserts adicionais sobre mensagem e causa.
1675. [[junit4-expected-peril]] — O parâmetro expected da anotação Test aceita subclasses de Throwable, mas a página oficial crava o problema: o teste passa se qualquer código do método lançar aquela exceção, e não dá para verificar a mensagem nem o estado do objeto depois do lançamento — "The expected parameter should be used with care".
1676. [[junit4-timeout-two-ways]] — Há duas formas documentadas: o parâmetro timeout no @Test, que roda o método em uma thread separada e, ao estourar o limite em milissegundos, falha o teste e interrompe a thread; e a regra Timeout, aplicada a todos os métodos da classe, hoje executada adicionalmente ao parâmetro individual.
1677. [[junit4-temporaryfolder]] — A regra TemporaryFolder cria arquivos e pastas que são deletados quando o método termina, passe ou falhe; por padrão nenhuma exceção é lançada se o recurso não puder ser apagado. O guia documenta newFile com nome, newFolder com nomes recursivos e as variantes aleatórias sem argumento.
1678. [[junit4-rules-collection]] — A página Rules define o propósito do mecanismo — adicionar ou redefinir de forma flexível o comportamento de cada método de teste, com a opção de estender as regras fornecidas ou escrever a sua — e documenta quatro utilitárias: ExternalResource para conectar recursos antes e desconectar depois (override before/after), ErrorCollector para continuar após o primeiro problema e reportar todos juntos, Verifier para transformar teste verde em falha ao final, TestWatcher para observar ações sem modificá-las.
1679. [[junit4-parameterized]] — O runner customizado Parameterized roda, conforme a página oficial, "instances are created for the cross-product of the test methods and the test data elements": o método estático anotado @Parameters devolve uma Collection de vetores de Object, e cada instância do teste é construída pelo construtor que recebe os valores de uma linha.

### ApprovalTests — verificação por aprovação com arquivos received e approved

1680. [[approvaltests-capturing-human-intelligence]] — O README oficial se abre com "Capturing Human Intelligence" e define o ApprovalTests como biblioteca open source de asserção/verificação para ajudar testes unitários, usada quando o objeto exige "more than a simple assert" — coleções, strings longas, logs, JPanels, XML, HTML, JSON e até colocar código legado sob teste.
1681. [[approvaltests-received-approved]] — O fluxo documentado: ao rodar, o teste gera YourTestClass.yourTestMethod.received.txt (ou png, html etc.) ao lado do teste, e o teste passa quando esse conteúdo coincide com o arquivo .approved correspondente; se os arquivos coincidem, o received é apagado — a presença de um .received no diretório é a falha, materializada.
1682. [[approvaltests-verify-and-verifyall]] — O tutorial mostra a separação: todo teste tem a parte Do e a parte Verify, e a verificação no ApprovalTests é Approvals.verify(objetoToBeVerified) — para sequências, Approvals.verifyAll(label, itens) imprime cada elemento indexado sob o rótulo dado, por exemplo Text[0] = Approval e Text[1] = Tests.
1683. [[approvaltests-json-objects]] — Para objetos sem toString útil — ou quando criar um não é desejável — o tutorial documenta JsonApprovals.verifyAsJson(objeto), que serializa o conteúdo e produz um arquivo de aprovação com extensão .json, por exemplo as chaves x, y, width e height do Rectangle aprovado como documento JSON indentado.
1684. [[approvaltests-awt-image]] — O tutorial documenta AwtApprovals.verify(componente) para qualquer herdeiro de java.awt.Component: o teste constrói a UI por código (o exemplo expõe um método selectTime em vez de clicar na interface) e o resultado verificado é um screenshot PNG do painel, aprovado como arquivo de imagem.
1685. [[approvaltests-combinations]] — Para ampliar cobertura sem escrever loops, o tutorial apresenta CombinationApprovals.verifyAllCombinations(lambda, arraysDeParametros): você declara um array de valores possíveis por parâmetro — até nove parâmetros — e a biblioteca executa a função em todas as combinações, aprovando a tabela inteira como um único artefato.
1686. [[approvaltests-reporters]] — Quando uma aprovação falha, um reporter é invocado para apresentar received e approved; o mecanismo de escolha é a anotação @UseReporter(Reporter.class) no método ou na classe, e a tabela oficial lista os reporters comuns com suas funções exatas.
1687. [[approvaltests-java-fitness]] — As três primeiras linhas técnicas do README oficial fixam a base: biblioteca de asserção/verificação open source, compatível com JUnit 3, 4 e 5 e com TestNG, funcionando em JDK 1.8+ com a lista testada 1.8, 17, 21, 24, 25 e 26 — e a nota de licença registra Apache 2.0.
1688. [[approvaltests-legacy-code]] — O README enumera "Getting Legacy Code under tests" entre os usos empacotados e, na seção Examples, registra a filosofia: "ApprovalTests eats its own dogfood" — os melhores exemplos da biblioteca estão no próprio código-fonte do repositório.
1689. [[approvaltests-no-checked-exceptions]] — A seção More Info do README oficial declara a filosofia "No Checked Exceptions": a API do ApprovalTests lança apenas exceções de runtime — com documento explicativo no repositório — porque um assistente de verificação que força try/catch no teste contaminaria justamente o código que deveria permanecer leitura pura de intenção.

### Fuzzing nativo em Go — testing.F, corpus e minimização na toolchain

1690. [[gofuzz-what-it-is]] — A documentação oficial define: o Go suporta fuzzing na sua toolchain padrão a partir do Go 1.18, e descreve fuzzing como testes automatizados que manipulam continuamente as entradas do programa para achar bugs, usando guidance por cobertura para percorrer o código de forma inteligente — com valor destacado para exploits e vulnerabilidades, "edge cases which humans often miss".
1691. [[gofuzz-test-requirements]] — A seção Requirements da doc oficial enumera o que um fuzz test deve cumprir: ser uma função com nome no estilo FuzzXxx, aceitar apenas uma testing.F e não retornar valor; viver em arquivos _test.go; conter exatamente um fuzz target, que é a chamada a (*testing.F).Fuzz recebendo *testing.T como primeiro parâmetro, seguido dos argumentos de fuzzing, sem retorno.
1692. [[gofuzz-argument-types]] — A doc oficial restringe os fuzzing arguments a um conjunto fechado: string e slice de byte; os inteiros de 8 a 64 bits com seus aliases rúne e byte; os uint correspondentes; float32 e float64; e bool — nada além disso pode aparecer após o *testing.T no fuzz target.
1693. [[gofuzz-seed-corpus]] — O seed corpus de um fuzz test é definido pela doc oficial como a composição das entradas passadas a (*testing.F).Add dentro do próprio teste com os arquivos do diretório testdata/fuzz/{NomeDoFuzzTest} do pacote — e a regra dura: os tipos de toda entrada seed devem ser idênticos aos argumentos do fuzzing, na mesma ordem, nos dois canais.
1694. [[gofuzz-corpus-format]] — A doc especifica a codificação dos arquivos de corpus, idêntica para seed e corpus gerado: a primeira linha informa a versão do formato — go test fuzz v1 — e cada linha seguinte traz um valor no formato de expressão Go, por exemplo []byte com notação de escapes e int64(572293), devendo casar os tipos dos argumentos de fuzzing, em ordem; "can be copied directly into Go code".
1695. [[gofuzz-two-modes]] — A doc separa explicitamente os modos: rodar o fuzz test como teste unitário (padrão do go test, executando as entradas do seed corpus e reportando falhas antes de sair) ou habilitar o fuzzing com go test -fuzz=Regex, onde o regex deve casar exatamente um fuzz test; por padrão, todos os outros testes do pacote rodam antes do fuzzing começar.
1696. [[gofuzz-output-metrics]] — A doc interpreta o log do fuzzing linha a linha: as primeiras linhas mostram o gathering baseline coverage, quando o motor executa os corpora seed e gerado para garantir que não há erros e entender que cobertura o corpus já traz; depois cada linha periódica traz elapsed, execs (com taxa por segundo) e new interesting — entradas que expandiram a cobertura além do corpus gerado.
1697. [[gofuzz-failure-causes]] — A seção Failing input lista as quatro causas de falha durante o fuzzing: panic no código ou no teste; chamada a t.Fail (inclusive via t.Error/t.Fatal); erro não recuperável como os.Exit ou stack overflow; e o alvo ter demorado demais — o timeout de execução do fuzz target é atualmente 1 segundo, podendo capturar deadlock ou loop infinito, ou comportamento intencional lento.
1698. [[gofuzz-minimization-regression]] — Quando um input falha, a doc descreve o fluxo: o motor tenta minimizar para o menor valor ainda reprodutível e mais legível a humanos, loga o erro e grava a entrada em testdata/fuzz/{FuzzTestName}/{hash} — a partir daí, aquele input roda pelo go test padrão, "serving as a regression test once the bug has been fixed", e a doc formula o próximo passo: diagnosticar, corrigir e submeter o patch com o arquivo novo como teste de regressão.
1699. [[gofuzz-cache-and-ossfuzz]] — A doc separa os dois corpora com nomes e endereços: o seed corpus — f.Add mais testdata/fuzz — é versionado e roda sempre; o generated corpus, mantido pelo motor durante a campanha para registrar progresso, fica em $GOCACHE/fuzz e "só é usado durante o fuzzing" — nada em que o pipeline normal deva depender.

### cargo-fuzz — fuzzing libFuzzer para crates Rust via subcommand do cargo

1700. [[cargofuzz-what-it-is]] — O README oficial define o projeto em uma linha: "A cargo subcommand for fuzzing with libFuzzer! Easy to use!" — em vez de montar manualmente os flags do clang com sanitizer, o usuário instala um binário cargo e ganha um fluxo de fuzzing nativo do ecossistema de crates.
1701. [[cargofuzz-platform-limits]] — O README lista as dependências duras do subcomando com franqueza: o libFuzzer precisa de suporte a sanitizers LLVM, então funciona apenas em x86-64 e Aarch64, apenas em sistemas Unix-like (Windows não), e exige um compiler nightly porque usa flags de linha de comando instáveis; adicionalmente, um compilador C++ com suporte a C++11 é necessário.
1702. [[cargofuzz-init-workspace]] — O comando cargo fuzz init prepara o projeto de fuzzing para o seu crate; o README oficial destaca a decisão estrutural: por default o diretório fuzz gerado é parte do workspace existente — e para crates em workspace é preciso adicionar fuzz à lista workspace.members do Cargo.toml raiz — ou você declara workspace independente com cargo fuzz init --fuzzing-workspace=true.
1703. [[cargofuzz-target-anatomy]] — O tutorial oficial constrói o target canônico: o arquivo em fuzz/fuzz_targets começa com #![no_main] e extern crate libfuzzer_sys, importa a crate sob teste e registra o alvo com a macro fuzz_target! recebendo um closure cujo parâmetro é uma fatia &[u8] de bytes pseudoaleatórios.
1704. [[cargofuzz-run-crash]] — O subcomando cargo fuzz run alvo começa a fuzzagem; o tutorial oficial interpreta o output como gerado pelo libFuzzer e exemplifica as linhas de progresso: número de execução, marcador NEW, cov (borda de cobertura), corp (entradas e bytes do corpus), exec/s e o que mudou de mutação (MS: EraseBytes, CopyPart etc.) — o output "looks like" exatamente aquilo enquanto o motor encontra caminhos novos.
1705. [[cargofuzz-list-add]] — Os dois subcomandos de gestão declarados no README oficial completam o ciclo de autor: cargo fuzz add <target> cria um novo alvo de fuzzing no projeto já inicializado, e cargo fuzz list exibe a lista de todos os alvos existentes — o tutorial do book o usa logo após o init para confirmar o target gerado.
1706. [[cargofuzz-fmt-arbitrary]] — O README oficial descreve o subcomando de inspeção: cargo fuzz fmt <target> <input> imprime a saída std::fmt::Debug de um test case, e destaca a utilidade quando o fuzz target aceita entrada Arbitrary — o tipo estruturado que o motor desserializa dos bytes crus.
1707. [[cargofuzz-tmin-cmin]] — O README define os dois redutores de forma simétrica: cargo fuzz tmin <target> <input> — "Found a failing input? Minify it to the smallest input that causes that failure" — e cargo fuzz cmin <target>, que minifica o corpus de arquivos de input inteiro, descartando os que não pagam seu aluguel na cobertura.
1708. [[cargofuzz-coverage-docs]] — O subcomando de medição declarada no README é cargo fuzz coverage <target>, que gera "coverage information on the fuzzed program"; a referência completa de flags fica em cargo fuzz --help, e o README aponta o Rust Fuzz Book em rust-fuzz.github.io como documentação de projeto — o book é o canônico, o README é o cartão de visita.
1709. [[cargofuzz-trophy-license]] — A seção Trophy Case do README oficial mantém a cultura do ecossistema: uma lista de bugs encontrados pelo cargo fuzz (e outros fuzzers) vive no repositório rust-fuzz/trophy-case, com o convite explícito para adicionar o seu; a licença é dupla, "both the MIT license and the Apache License (Version 2.0)", com os textos LICENSE-MIT e LICENSE-APACHE no próprio repo.

### AFL++ — o fork de referência do AFL com instrumentação, cmplog e campanhas paralelas

1710. [[aflpp-what-it-is]] — O README oficial se define como "a superior fork to Google's AFL — more speed, more and better mutations, more and better instrumentation, custom module support", mantém numeração de release (5.03c na página atual, com página de Releases) e credita a manutenção a Marc Heuse, Dominik Maier, Andrea Fioraldi e Heiko Eissfeldt, com o AFL original de Michal Zalewski.
1711. [[aflpp-license-docker-branches]] — O README oficial documenta uma estrutura de licença dupla deliberada: o AFL++ é AGPL-3.0-or-later e contém arquivos Apache-2.0, mas "Everything compiled into a fuzzing harness is and will stay Apache 2.0 licensed", cada arquivo declara sua licença em cabeçalho SPDX — e uma licença comercial opcional existe para quem não pode usar AGPL, obtida por doação ("the project and its maintainers receive no money").
1712. [[aflpp-compiler-modes]] — O guia in-depth formaliza a escolha do compilador de instrumentação: um fluxo de decisão que começa em clang/clang++ 11+ (modo LTO, afl-clang-lto), cai para clang 3.8+ (modo LLVM, afl-clang-fast) e depois para gcc 5+ com suporte a plugin (GCC_PLUGIN, afl-gcc-fast), encerrando com "GAME OVER! Install gcc-plugin-dev ou llvm-dev" quando nada existe; o aviso na página é seco — afl-gcc e afl-clang puros foram removidos por obsolescência.
1713. [[aflpp-instrumentation-options]] — A seção de opções de instrumentação do guia oficial descreve duas famílias: laf-intel/COMPCOV — split de comparações de inteiros, strings, floats e switches, ativado com AFL_LLVM_LAF_ALL=1 antes de compilar, "importante se você não tem um corpus bom e grande" — e o cmplog/redqueen, "usualmente melhor que laf-intel": instrumenta o alvo para reportar valores comparados, com AFL_LLVM_CMPLOG=1 na compilação e consumo via -c, avisando que usar o mesmo binário para fuzz normal e cmplog custa uns 20% de performance, melhor compilando um segundo binário cmplog apontado por -c.
1714. [[aflpp-sanitizers]] — O guia dedica uma seção a sanitizers com a filosofia explícita: encontrar bugs "that would not necessarily result in a crash"; a doc enumera o suporte embutido com suas variáveis — AFL_USE_ASAN (use-after-free, NULL deref, overruns), AFL_USE_MSAN (leituras de memória não inicializada), AFL_USE_UBSAN (comportamento indefinido pelo padrão C/C++), AFL_USE_CFISAN (confusão de tipos, herdeiro da detecção anti-ROP), AFL_USE_TSAN (corridas) e AFL_USE_LSAN (vazamentos, com os hooks __AFL_LEAK_CHECK e as chaves __AFL_LSAN_OFF/ON).
1715. [[aflpp-target-modification]] — A seção "d) Modifying the target" ensina a intervenção canônica: remover (ou neutrar) verificações que bloqueiam o fuzzer — checksums, HMAC — dentro de blocos #ifdef FUZZING_BUILD_MODE_UNSAFE_FOR_PRODUCTION, definição que todos os compiladores AFL++ ligam automaticamente, permitindo o hack "só no build de fuzz" em código usado em produção.
1716. [[aflpp-corpus-prep]] — A segunda parte do guia é um ritual de três ferramentas para o insumo do afl-fuzz: coletar o máximo de entradas válidas possível de qualquer fonte (a doc sugere bugs reportados, test suites, downloads aleatórios, dados de unit test — e o diretório testcases/ do repo); deduplicar com afl-cmin -i INPUTS -o INPUTS_UNIQUE mantendo só o que produz caminho novo, com @@ para alvo por arquivo e stdin como default sem @@; e opcionalmente minimizar cada arquivo com afl-tmin num loop (paralelizável com GNU parallel), porque "the shorter the input files... the better the fuzzing".
1717. [[aflpp-run-basics]] — Antes de qualquer run, o guia manda rodar sudo afl-system-config — que reconfigura o sistema para performance de fuzzing e sem o qual o afl-fuzz bails — com o fallback documentado AFL_SKIP_CPUFREQ=1 quando não há root; em Docker, a doc recomenda passar --cpuset-cpus com cores livres ou AFL_NO_AFFINITY, porque cada container vê só seus cores e todos os afl-fuzz mirariam o mesmo core sem isso.
1718. [[aflpp-dictionaries-memory]] — A doc de dicionários do guia começa pela pergunta "já existe?" — o diretório dictionaries/ do repositório cobre formatos conhecidos e entra via -x dictionaries/FORMAT.dict; mas o AFL++ também gera dicionário sozinho: com afl-clang-lto é autodictionary sem esforço nenhum, com afl-clang-fast usa-se AFL_LLVM_DICT2FILE=/caminho/novo.dic na compilação (mais AFL_LLVM_DICT2FILE_NO_MAIN=1 para ignorar parsing de argv, "often a good idea"), e a alternativa offline é o utils/libtokencap capturando tokens durante uma execução independente — ou escrever o .dic à mão.
1719. [[aflpp-parallel-campaign]] — A seção de múltiplos cores do guia define a topologia canônica: um main fuzzer (-M main-$HOSTNAME com AFL_FINAL_SYNC=1) e um secondary (-S nome-qualquer) por core útil, todos compartilhando o mesmo diretório -o — nomes únicos por instância, o mesmo output para todas; e a doc marca um teto por máquina, "entre 32 e 64 cores", além do qual adicionar instâncias degrada o performance global.

### boofuzz — fuzzing de protocolos de rede com Requests, grafo de estados e SQLite

1720. [[boofuzz-successor-of-sulley]] — O README oficial define o projeto: "a fork of and the successor to the venerable Sulley fuzzing framework", que, além de correções de bugs, mira extensibilidade — "The goal: fuzz everything" — e justifica a existência porque o Sulley, por anos o fuzzer open source preeminente, caiu em desmanutenção; o nome homenageia o único personagem que assustou o próprio Sulley no Monstros S.A.
1721. [[boofuzz-session-target]] — A doc de quickstart abre com a definição operacional: o objeto Session é "the center of your fuzz… session", criado com um Target que, por sua vez, recebe um objeto de Connection — o exemplo canônico é uma Session com Target com TCPSocketConnection apontando para 127.0.0.1 porta 8021.
1722. [[boofuzz-request-grammar]] — Após ler o RFC, a página manda "define your protocol using the various block and primitive types": cada mensagem é um Request nomeado cujos filhos descrevem a estrutura, e o exemplo do FTP constrói user, pass, stor e retr idênticos — String para os campos mutáveis, Delim("space", " ") como separador e Static("end", ...) com o terminator CRLF da linha.
1723. [[boofuzz-state-graph]] — Com as mensagens definidas, o mesmo Quickstart conecta tudo à Session: session.connect(user); session.connect(user, passw); session.connect(passw, stor); session.connect(passw, retr) — e a doc traduz a semântica em uma frase: ao fuzzar, o boofuzz "will send user before fuzzing passw, and user and passw before fuzzing stor or retr".
1724. [[boofuzz-fuzz-run]] — Depois de conexão e grafo, o gatilho é literalmente session.fuzz(); e a página tem o cuidado raro de avisar logo abaixo: "at this point you have only a very basic fuzzer. Making it kick butt is up to you", apontando para os dois diretórios do repositório que servem de curriculum: examples/ e request_definitions/.
1725. [[boofuzz-results-sqlite]] — A persistência documentada no Quickstart: o log de dados de cada run é salvo em um banco SQLite dentro do diretório boofuzz-results no diretório de trabalho atual — e a qualquer momento é possível reabrir a interface web sobre um daqueles arquivos com boo open <run-*.db>.
1726. [[boofuzz-callbacks]] — Para "cool stuff like checking responses" — a frase da doc — a Quickstart manda usar post_test_case_callbacks na Session, e para usar dados de uma resposta numa requisição subsequente, aponta a classe ProtocolSessionReference; o README, por sua vez, anuncia "Extensible instrumentation/failure detection" como feature central, da qual esses hooks são a face pública.
1727. [[boofuzz-monitors]] — O repositório oficial carrega os monitores como arquivos de topo nomeados: process_monitor.py e process_monitor_unix.py (watchdog de processo-alvo, com variante unix) e network_monitor.py — correspondendo ao par de capacidades que o README lista como elementos críticos de um fuzzer: "Instrumentation – AKA failure detection" e "Target reset after failure".
1728. [[boofuzz-install-python]] — A seção Installation do README oficial é um bloco só — pip install boofuzz — seguida da chave conceitual: "Boofuzz installs as a Python library used to build fuzzer scripts", com a página INSTALL.rst reservada para "advanced and detailed instructions"; a linha de versão da doc atual carrega o release 0.4.2 nas páginas renderizadas.
1729. [[boofuzz-docs-sources]] — A cadeia de documentação do boofuzz tem quatro degraus explícitos: o README.rst no repositório jtpereyda/boofuzz, a documentação completa em boofuzz.readthedocs.io ("including nifty quickstart guides", frase do próprio README), os diretórios examples/ e request_definitions/ do repositório como biblioteca de fuzzers reais — do Ultra MiniHTTPd ao Oracle 9i XDB nos roteiros públicos — e o tag fuzzing no Stack Overflow como canal de suporte nomeado pelo projeto.

### Hyperfoil — benchmark distribuído de microsserviços com modelo aberto e YAML

1730. [[hyperfoil-what-it-is]] — A página inicial oficial define o projeto como um "microservice-oriented distributed benchmark framework" com quatro bandeiras declaradas: distributed (o load vem de muitos nodes), accurate (todas as operações são assíncronas para evitar a coordinated-omission fallacy), versatile (cenários complexos em YAML ou steps plugáveis) e low-allocation (alocar o mínimo nos caminhos críticos para o garbage collector não perturbar as operações).
1731. [[hyperfoil-apache-license]] — A seção Free software do Overview oficial faz do licenciamento um argumento metodológico: "Free software allows you to take your benchmark and publish it for everyone to verify. With proprietary licenses that wouldn't be so easy" — e o Hyperfoil é distribuído sob a Apache License 2.0, com link para o texto.
1732. [[hyperfoil-open-system]] — O Overview é pedagógico sobre o problema: benchmarks medem o que acontece com milhares de usuários concorrentes cada um fazendo loads espaçados, mas drivers tradicionais simplificam para dezenas de VUs executando um request após outro ou com atrasos mínimos — o Closed System Model — o que produz latências enviesadas e deixa de disparar condições patológicas (queues estourando), problema conhecido como coordinated omission (com o slide How Not to Measure Latency linkado em dois lugares do site).
1733. [[hyperfoil-leader-follower]] — O modelo de distribuição documentado: Hyperfoil usa um líder e seguidores (leader-follower) com o Vert.x Event Bus como middleware de clustering — o Controller é o servidor Vert.x com API REST que tem o papel de líder: ao iniciar um benchmark, ele faz deploy dos agents conforme a definição do benchmark, empurra a definição para eles e orquestra as fases; os agents executam o benchmark e mandam estatísticas periodicamente, permitindo ao controller combinar e avaliar tudo on the fly; quando o benchmark termina, todos os agents terminam.
1734. [[hyperfoil-phases]] — O Concepts documenta que um benchmark consiste de várias fases; fases podem rodar independentemente uma da outra simulando cargas de grupos de usuários diferentes (o exemplo: visitors versus admins) e, dentro de uma fase, todos os usuários executam o mesmo cenário (exemplo: logar, vender todo o estoque, sair); fases também são o instrumento de escala — buscar throughput máximo significa agendar várias iterações da mesma fase aumentando gradualmente o número de usuários.
1735. [[hyperfoil-sessions-prealloc]] — O modelo de estado do Hyperfoil é a session: "the state of each user's scenario is saved in the session; sometimes we speak about (re)starting sessions instead of starting new users" — e a página conecta a abstração diretamente com a política low-allocation: o benchmark pré-aloca toda a memória da execução do cenário adiante, o que implica que todos os recursos são limitados por pools (o sistema precisa saber os tamanhos).
1736. [[hyperfoil-scenario-steps]] — O Concepts fecha a hierarquia do benchmark com analogia de programação: o cenário consiste de uma ou mais sequências compostas de steps — "steps are similar to statements in programming language and sequences are an equivalent of blocks of code" — e, como um navegador real executa parte das operações em paralelo (imagens carregando concorrentes num page load), a sessão contém a qualquer momento uma ou mais sequence instances ativas, encerrando quando todas terminam para reciclar o usuário.
1737. [[hyperfoil-first-run]] — O Quickstart 1 oficial conduz o primeiro benchmark em quatro passos mecânicos: baixar e descompactar o release (exemplo com a versão 0.29.3 do GitHub Hyperfoil/Hyperfoil releases), iniciar o modo interativo com bin/cli.sh, digitar start-local para subir um controller embutido (saída mostra o controller ouvindo em 127.0.0.1:41621 e a conexão estabelecida) e então upload de um arquivo single-request.hf.yaml seguido de run nomeando o benchmark.
1738. [[hyperfoil-stats]] — O output do comando stats no Quickstart 1 oficial é uma tabela com cabeçalho denso: PHASE, METRIC, REQUESTS, MEAN, p50, p90, p99, p99.9, p99.99, colunas de contagem por classe de resposta (2xx, 3xx, 4xx, 5xx) e os quatro medidores de falha de infraestrutura do lado do driver: CACHE, TIMEOUTS, ERRORS e BLOCKED — com o rodapé Total stats from run agregando os agents.
1739. [[hyperfoil-extensions-api]] — O índice oficial da documentação organiza o produto em nove seções, e três delas definem o teto de extensibilidade: Controller API (OpenAPI 3 specification do controller), Extensions (como desenvolver suas próprias extensões) e Custom components no Quickstart 8 — a porta para escrever a lógica em Java "ou qualquer outra linguagem JVM" quando o DSL YAML aperta, além da seção Migration para quem vem de outras ferramentas.

### Infection — mutation testing para PHP com MSI, mutators AST e integração de CI

1740. [[infection-what-mutation-testing]] — O guia oficial define mutation testing como técnica baseada em fault com o critério MSI (Mutation Score Indicator): modificar o programa em pequenas formas — cada versão modificada é um mutante — e executar os mutantes contra a suíte de testes para ver se as falhas semeadas são detectadas; mutante com teste vermelho é "killed", mutante com testes verdes é "escaped", e suítes são medidas pela porcentagem de mutantes que matam.
1741. [[infection-what-infection]] — A definição oficial: "Infection is a PHP mutation testing library based on AST (Abstract Syntax Tree) mutations. It works as a CLI tool and can be executed from your project's root", com o resumo do algoritmo em cinco passos — rodar a suíte para confirmar que passa, mutar o código-fonte com os mutadores predefinidos, para cada mutante rodar os testes que cobrem a linha modificada, analisar se os testes passaram a falhar, e coletar os resultados de killed, escaped, erros e timeouts.
1742. [[infection-msi-metrics]] — O Introduction oficial descreve o bloco Metrics com as fórmulas: MSI é TotalDefeatedMutants (KilledCount + TimedOutCount + ErrorCount) dividido pelo TotalMutantsCount — 47% no exemplo — "the primary Mutation Testing metric"; Mutation Code Coverage é a fatia de mutantes coberta por algum teste (TotalMutants - NotCoveredByTests)/TotalMutants, 67% no exemplo, que "on average should be within the same ballpark as your normal code coverage"; e Covered Code MSI restringe o numerador ao denominador coberto — 70% no exemplo, "ignoring not tested code", mostrando "how effective the tests really are".
1743. [[infection-install-phar]] — A página Installation oficial recomenda o phar como "the best and recommended way": baixar infection.phar mais infection.phar.asc do release (exemplo com a versão 0.32.0), chmod +x e — o diferencial de supply-chain — verificar a assinatura com as duas linhas gpg (recv-keys da chave C6D76C329EBADE2FB9C458CFC5095986493B4AA0 e --with-fingerprint --verify), conferindo que o fingerprint bate; o phar é assinado com a chave GPG do time, com o link da chave pública no site.
1744. [[infection-threads]] — A seção de threads da doc oficial de opções prescreve --threads (ou -j) maior que 1 para rodar os testes dos códigos mutados em paralelo — "it will dramatically speed up mutation process" — e documenta o --threads=max para autodetecção de cores, além do receituário antigo para versões < 0.26.15 (infection -j$(nproc) no Linux, $(sysctl -n hw.ncpu) no macOS).
1745. [[infection-reuse-coverage]] — A justificativa da opção --coverage na doc oficial é de custo puro: quem roda CI com Xdebug/phpdbg para gerar métricas de cobertura e depois roda Infection está executando a suíte com debugger duas vezes, o que "dramatically increases the build time"; com --coverage=<path> o Infection consome os relatórios já gerados.
1746. [[infection-git-diff]] — A doc oficial das opções documenta o recorte por git como o modo CI de primeira classe: --git-diff-filter aplica git diff com --diff-filter para filtrar os arquivos a mutar, com os valores sensatos AM (adicionados e modificados) e A (só adicionados), e a página prescreve o par com o fetch raso do base branch (git fetch --depth=1 origin $GITHUB_BASE_REF) no GitHub Actions antes de rodar infection.phar --git-diff-filter=A.
1747. [[infection-loggers]] — A doc oficial de opções descreve quatro saídas integráveis: --logger-github, que imprime GitHub Annotation warnings para mutantes escapados direto no pull request — com detecção automática do ambiente GitHub Actions, forçamento por =true/=false e o link do próprio workflow de exemplo do projeto — ; --logger-gitlab, que grava um Code Quality report (Code Climate) em arquivo json, consumível como artifact; --logger-html, que gera um relatório HTML navegável com exemplo hospedado no site; e --logger-text, que aceita caminhos físicos e também php://stdout, php://stderr e php://output para pipelines que capturam buffer.
1748. [[infection-mutators]] — A página Mutators oficial documenta que os mutadores do Infection são baseados em AST sobre o projeto PHP-Parser de nikic, organizados em famílias com tabelas Original/Mutated: a seção Function Signature cobre PublicVisibility (público vira protected) e ProtectedVisibility (protected vira private) com a tese de encapsulamento (visibilidade redutível é API pública maior que o necessário); a família Unwrap* desfaz centenas de funções de array e string (UnwrapArrayChunk passa a lista sem o chunk); Binary Arithmetic troca operadores (+ vira -, % vira *, &= vira =); e a Round Family troca round, floor e ceil entre si "to make sure there's enough tests to cover the rounding possibilities".
1749. [[infection-test-framework]] — A doc de opções documenta o seletor de motor de teste: --test-framework recebe o nome do framework a usar, com a lista oficial PHPUnit, PhpSpec, Codeception e Testo, e a regra de disponibilidade dos adaptadores — na instalação composer, o PHPUnit já vem; os demais adaptadores são instalados sob demanda, enquanto a distribuição phar carrega todos os disponíveis de fábrica.

### Atheris — fuzzing nativo de Python com cobertura, mutators custom e libFuzzer

1750. [[atheris-what-it-is]] — O README oficial define: "Atheris is a coverage-guided Python fuzzing engine. It supports fuzzing of Python code, but also native extensions written for CPython", construído sobre o libFuzzer — e, ao fuzzar código nativo, combinável com AddressSanitizer ou UndefinedBehaviorSanitizer para pegar bugs adicionais.
1751. [[atheris-install-platform]] — O README fixa o suporte: Linux de 32 e 64 bits e Mac OS X, Python 3.11 a 3.14 na fonte atual (versões 3.10 e abaixo "remain accessible in PyPI" mas não no código-fonte corrente), e a instalação padrão via pip3 install atheris traz wheels com um libFuzzer built-in que é "fine for fuzzing Python code".
1752. [[atheris-minimal-harness]] — O exemplo oficial é o esqueleto completo: importar atheris, abrir um bloco with atheris.instrument_imports(): importando a lib sob teste, definir TestOneInput(data) que chama a função de parsing, e fechar com atheris.Setup(sys.argv, TestOneInput) mais atheris.Fuzz() — quatro peças e nada além delas.
1753. [[atheris-instrumentation-modes]] — O README enumera as três formas de inserir a instrumentação de cobertura no bytecode: o bloco instrument_imports() (que propaga às libs importadas e às que estas importam), o decorator @atheris.instrument_func por função, e atheris.instrument_all(), que varre todo o interpretador e instrumenta toda função Python carregada — "put this right before atheris.Setup()", com o aviso de que "might take a while".
1754. [[atheris-no-interesting]] — A seção homônima do README documenta o erro — ERROR: no interesting inputs were found. Is the code instrumented for coverage? — com o mecanismo exato: ele aparece quando as duas primeiras chamadas a TestOneInput não produziram nenhum evento de cobertura, e isso acontece mesmo com instrumentação existente, por exemplo quando o TestOneInput é nontrivial e a cobertura instrumentada não é alcançada nos dois primeiros inputs.
1755. [[atheris-coverage-viz]] — A página documenta a compatibilidade com o coverage.py: roda-se o fuzzer sob python3 -m coverage run your_fuzzer.py -atheris_runs=10000, seguido de coverage html para gerar o relatório navegável — com a razão declarada: examinar quais linhas são executadas ajuda a entender a efetividade do fuzzer, no mesmo modelo visual usado para qualquer programa Python.
1756. [[atheris-setup-api]] — A seção API do README oficial especifica as assinaturas centrais: Setup(args, test_one_input, internal_libfuzzer=None) — onde args são os strings de processo (tipicamente sys.argv) que podem ser modificados in-place para remover os argumentos consumidos pelo fuzzer (a lista de flags é a da documentação do libFuzzer, linkada), test_one_input precisa receber exatamente um bytes, e internal_libfuzzer diz se o libFuzzer vem do Atheris ou de uma lib externa, auto-determinado quando não especificado, com a instrução explícita: fuzzing de Python puro, deixe como True.
1757. [[atheris-fuzzeddataprovider]] — A página oficial documenta o equivalente Python do utilitário homônimo do libFuzzer: construído com atheris.FuzzedDataProvider(input_bytes), ele oferece uma família de Consume* que materializa a sequencia de bytes em valores — ConsumeBytes, ConsumeUnicode (com surrogate pairs possíveis, "invalid per spec but needed por ferramentas como paths no Windows", na explicação da página), ConsumeUnicodeNoSurrogates, ConsumeString (alias de Unicode no Python 3), ConsumeInt/ConsumeUInt de tamanho configurável, ConsumeIntInRange, listas com e sem range, e floats incluindo "weird values like NaN and Inf" no ConsumeFloat padrão, com ConsumeRegularFloat para os numéricos limpos.
1758. [[atheris-custom-mutator]] — A seção Structure-aware Fuzzing do README oficial admite a limitação do modelo — mutação pura em dados complexos morre na porta ("inputs will be rejected early, resulting in low coverage") — e a resposta são os custom mutators do libFuzzer, expostos como parâmetro custom_mutator de atheris.Setup; dentro dele, chama-se atheris.Mutate(data, len) (equivalente ao LLVMFuzzerMutate) para reutilizar a mutação nativa sobre a representação descompactada, compactando o resultado de volta.
1759. [[atheris-ossfuzz-native]] — A seção Integration with OSS-Fuzz oficial declara suporte pleno: "Atheris is fully supported by OSS-Fuzz, Google's continuous fuzzing service for open source projects", com a integração governada pela guide própria do OSS-Fuzz para Python (link new-project-guide/python-lang na doc do serviço) — ou seja, o caminho local do pip até a campanha contínua da Google existe como produto, não como promessa.

## Estado editorial

O gate automatizado foi aprovado por 1759/1759 notas e as 1759 contam como válidas pelo protocolo atualizado: nove têm aprovação humana histórica e 1750 têm revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (1759 notas substantivas; 241 ainda não produzidas). Consulte o [manifesto](../../exports/batches/software-testes-2000-0001.md), a [auditoria de qualidade](../../exports/reports/note-quality-software-testes-2000-0001.md) e a [reconciliação mais recente do manifesto/fila](../../exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-23.md)). Os relatórios factuais por IA são [tranches 2–3](../../exports/reports/ai-review-software-testes-2000-0001.md), [4](../../exports/reports/ai-review-software-testes-2000-0001-tranche-04.md), [5](../../exports/reports/ai-review-software-testes-2000-0001-tranche-05.md), [6](../../exports/reports/ai-review-software-testes-2000-0001-tranche-06.md), [7](../../exports/reports/ai-review-software-testes-2000-0001-tranche-07.md), [8](../../exports/reports/ai-review-software-testes-2000-0001-tranche-08.md), [9](../../exports/reports/ai-review-software-testes-2000-0001-tranche-09.md), [10](../../exports/reports/ai-review-software-testes-2000-0001-tranche-10.md), [11](../../exports/reports/ai-review-software-testes-2000-0001-tranche-11.md) e [12](../../exports/reports/ai-review-software-testes-2000-0001-tranche-12.md), [13](../../exports/reports/ai-review-software-testes-2000-0001-tranche-13.md), [14](../../exports/reports/ai-review-software-testes-2000-0001-tranche-14.md), [15](../../exports/reports/ai-review-software-testes-2000-0001-tranche-15.md), [16](../../exports/reports/ai-review-software-testes-2000-0001-tranche-16.md), [17](../../exports/reports/ai-review-software-testes-2000-0001-tranche-17.md), [18](../../exports/reports/ai-review-software-testes-2000-0001-tranche-18.md), [19](../../exports/reports/ai-review-software-testes-2000-0001-tranche-19.md), [20](../../exports/reports/ai-review-software-testes-2000-0001-tranche-20.md), [21](../../exports/reports/ai-review-software-testes-2000-0001-tranche-21.md), [22](../../exports/reports/ai-review-software-testes-2000-0001-tranche-22.md) e [23](../../exports/reports/ai-review-software-testes-2000-0001-tranche-23.md). Consulte também o [registro de revisão humana e IA](../../exports/reports/human-review-queue.md).
